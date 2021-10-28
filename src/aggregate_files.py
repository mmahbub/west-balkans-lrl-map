#!/usr/bin/env python

import argparse
from pathlib import Path

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description="Script to aggregate language files across different documents into a single file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-p', '--path', type=str, help='Directory containing sub-directories corresponding to different documents', required=True)
  return parser.parse_args()

if __name__=='__main__':
  args = parse_args()
  path = Path(args.path)
  # langs = str(path.stem).split('-')
  data = {}  

  for doc_dir in path.iterdir():
    print(doc_dir)
    for lang_file in doc_dir.glob('*.txt'):
      print(lang_file)
      with open(lang_file, 'r') as f:
        content = f.readlines()      
    break

  print(len(content))
    
    

