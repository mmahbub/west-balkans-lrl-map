#!/usr/bin/env python

import math, sys, subprocess, shutil
from typing import Dict, List
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from pathlib import Path

def parse_args() -> Namespace:
  parser = ArgumentParser(description="Script to prepare manually extracted data to be loaded into HuggingFace hub. Please see README for details.", formatter_class=ArgumentDefaultsHelpFormatter)
  parser.add_argument('dir', type=str, help='Directory containing sub-directories corresponding to different documents')
  parser.add_argument('-p', '--test_pct', type=float, help='Percentage of test data', default=0.15)
  return parser.parse_args()

def write_content(path: Path, content: str)  -> None:
  with open(path, 'w') as f:
    content = '\n'.join(content)
    f.write(''.join(content))


def aggregate_files(path: Path) -> Dict[str, List[str]]:
  data = {lang: [] for lang in str(path.stem).split('-')}

  # NOTE: Using sorted guarantees order but loads everything into memory
  for doc_dir in sorted(path.iterdir()):
      for lang_file in doc_dir.glob('*.txt'):
        with open(lang_file, 'r') as f:
          content = f.readlines()
        data[lang_file.stem] += [line.strip() for line in content]

  for lang, content in data.items():
    write_content(path/f'{lang}.txt', content)

  return data

def huggingface_setup(path: Path, data: Dict[str, List[str]], test_pct: float) -> None:
  split_idx = math.ceil(test_pct * len(data['english']))

  for lang, content in data.items():
    data[lang] = {
      'train': content[split_idx:],
      'test': content[:split_idx],
    }

  temp_dir = path.parents[0]/'temp_dir'
  temp_dir.mkdir(exist_ok=True)
  data_files = {}

  for lang in path.stem.split('-'):
    if lang != 'english':
      dir_name = f'en-{lang[:2]}'
      data_files[dir_name] = {
        'english': {
          'train': temp_dir/dir_name/'train_en.txt',
          'test': temp_dir/dir_name/'test_en.txt',

        },
        f'{lang}': {
          'train': temp_dir/dir_name/f'train_{lang[:2]}.txt',
          'test': temp_dir/dir_name/f'test_{lang[:2]}.txt'
        }
      }

  for dir_name, lang_pair in data_files.items():
    for lang, splits in lang_pair.items():
      for split, fp in splits.items():
        fp.parent.mkdir(exist_ok=True)
        write_content(fp, data[lang][split])

  subprocess.call(['tar', '-C', temp_dir, '-cvzf', 'rosetta_balcanica.tar.gz', '.'])
  temp_dir.rmdir()

if __name__=='__main__':
  args = parse_args()
  path = Path(args.dir)
  test_pct = args.test_pct

  if test_pct < 0 or test_pct > 1:
    print(f"Test percentage must be between 0 and 1. Got {test_pct}", file=sys.stderr)
    sys.exit(1)

  data = aggregate_files(path)
  huggingface_setup(path, data, test_pct)