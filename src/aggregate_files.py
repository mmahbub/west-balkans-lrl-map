#!/usr/bin/env python

import argparse
from pathlib import Path

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description="Script to aggregate language files across different documents into a single file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-d', '--dir', type=str, help='Directory containing sub-directories corresponding to different documents', required=True)
  return parser.parse_args()

if __name__=='__main__':
  args = parse_args()
  path = Path(args.dir)
  print(path)
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