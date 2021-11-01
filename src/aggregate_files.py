#!/usr/bin/env python

import textwrap
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
  return parser.parse_args()


def aggregate_files():
  pass

if __name__=='__main__':
  args = parse_args()
  path = Path(args.dir)
  hf_hub_path = path.parents[0]/'huggingface_hub'
  hf_hub_path.mkdir(exist_ok=True)
  data = {lang: [] for lang in str(path.stem).split('-')}
  hf_dirs = {}
  for lang, _ in data.items():
    if lang != 'english':
      dir_name = f'en-{lang[:2]}'
      hf_dirs[dir_name] = hf_hub_path/dir_name

  for _, dirname in hf_dirs.items():
    dirname.mkdir(exist_ok=True)

  # for doc_dir in path.iterdir():
  #   for lang_file in doc_dir.glob('*.txt'):
  #     with open(lang_file, 'r') as f:
  #       content = f.readlines()
  #     data[lang_file.stem] += [line.strip() for line in content]
  
  # for lang, content in data.items():
  #   with open(path/f'{lang}.txt', 'w') as f:
  #     content = '\n'.join(content)
  #     f.write(''.join(content))  