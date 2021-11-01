#!/usr/bin/env python

import textwrap
from argparse import ArgumentParser, HelpFormatter, Namespace
from pathlib import Path

script_description = """
This script does the following:

  1. Aggregates language files across different documents into a single file
  2. Sets up the data to be using via HuggingFace's datasets library and hub with training and testing splits

This script needs to be run on a specific directory containing folders corresponding to each
document. These folders should contain text files associated with each language that is being processed.
There can be multiple languages per folder.

Multiple language files result in multiple datasets. For example, processing files inside english-macedonian-shqip
will result in:

  1. english.txt, macedonian.txt, shqip.txt in that folder
  2. en-ma and en-sh folders in datasets/huggingface_hub
  3. within each we will have train and test files for machine translation
"""

class RawFormatter(HelpFormatter):
  def _fill_text(self, text: str, width: int, indent: str) -> str:
      return '\n'.join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])
    

languages = ['english', 'macedonian', 'shqip']

def parse_args() -> Namespace:
  parser = ArgumentParser(description=script_description, formatter_class=RawFormatter)
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