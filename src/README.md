`aggregate_files.py` does the following:

  1. Aggregates language files across different documents into a single file

  2. Sets up the data to be using via HuggingFace's datasets library and hub with training and testing splits

This script needs to be run on a specific directory containing folders corresponding to each
document. These folders should contain text files associated with each language that is being processed.
There can be multiple languages per folder. Multiple language files result in multiple datasets. For example, processing files inside english-macedonian-shqip
will result in:

  1. english.txt, macedonian.txt, shqip.txt in that folder

  2. en-ma and en-sh folders in `datasets/huggingface_hub`

  3. within each we will have train and test files for machine translation