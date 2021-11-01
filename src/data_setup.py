#!/usr/bin/env python

import random, textwrap
from argparse import ArgumentParser, HelpFormatter, Namespace
from pathlib import Path

script_description = """
Script to prepare manually extracted data to be loaded into HuggingFace hub. Please see README for details.
"""

class RawFormatter(HelpFormatter):
  def _fill_text(self, text: str, width: int, indent: str) -> str:
      return '\n'.join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])
    

languages = ['english', 'macedonian', 'shqip']

def parse_args() -> Namespace:
  parser = ArgumentParser(description=script_description, formatter_class=RawFormatter)
  parser.add_argument('-d', '--dir', type=str, help='Directory containing sub-directories corresponding to different documents', required=True)
  parser.add_argument('-s', '--seed', type=int, help='Random seed to split the data into training and testing', default=42)
  return parser.parse_args()


def aggregate_files(path):
  data = {lang: [] for lang in str(path.stem).split('-')}  
  for doc_dir in path.iterdir():
      for lang_file in doc_dir.glob('*.txt'):
        with open(lang_file, 'r') as f:
          content = f.readlines()
        data[lang_file.stem] += [line.strip() for line in content]
    
  for lang, content in data.items():
    with open(path/f'{lang}.txt', 'w') as f:
      content = '\n'.join(content)
      f.write(''.join(content))

  return data

if __name__=='__main__':
  args = parse_args()
  path = Path(args.dir)
  random.seed(args.seed)

  data = aggregate_files(path)
  split_idx = random.randint(0, len(data['english']))

  for lang, content in data.items():
    data[lang] = {
      'train': content[:split_idx],
      'test': content[split_idx:],
    }

  hf_hub_path = path.parents[0]/'huggingface_hub'
  hf_hub_path.mkdir(exist_ok=True)  
  hf_files = {}

  for lang in path.stem.split('-'):
    if lang != 'english':
      dir_name = f'en-{lang[:2]}'
      hf_files[dir_name] = {
        'english': {
          'train': hf_hub_path/dir_name/'train_en.txt',
          'test': hf_hub_path/dir_name/'test_en.txt',

        },
        f'{lang}': {
          'train': hf_hub_path/dir_name/f'train_{lang[:2]}.txt',
          'test': hf_hub_path/dir_name/f'test_{lang[:2]}.txt'
        }
      }

  for dir_name, lang_pair in hf_files.items():    
    for lang, splits in lang_pair.items():
      for split, fp in splits.items():
        fp.parent.mkdir(exist_ok=True)
        with open(fp, 'w') as f:
          content = '\n'.join(data[lang][split])
          f.write(content)
      
  # from pprint import pprint
  # pprint(hf_files)
      
  # for _, dirname in hf_dirs.items():
  #   dirname.mkdir(exist_ok=True)

  # print(hf_dirs)
  # print(data.keys())




  # for lang in path.stem.split('-'):
  #   if lang != 'english':
  #     nen = lang[:2]
  #     dir_name = hf_hub_path/f'en-{nen}'
  #     dir_name.mkdir(exist_ok=True)
  #     print(dir_name)
  #     for split, content in data[lang].items():
  #       with open(dir_name/f'{split}_en.txt', 'w') as f:
  #         content = '\n'.join(content)
  #         f.write(content)
  #       with open(dir_name/f'{split}_{nen}.txt', 'w') as f:
  #         content = '\n'.join(content)
  #         f.write(content)


  #     with open(dir_name/'train_en.txt', 'w') as f:
  #       content = '\n'.join(data[lang])
  #     hf_dirs[dir_name] = hf_hub_path/dir_name


  

  