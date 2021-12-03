# Dataset for Low Resource West Balkan Languages

As of now, we have dataset for two West Balkan languages [Macedonian](https://en.wikipedia.org/wiki/Macedonian_language) and [Albanian](https://en.wikipedia.org/wiki/Albanian_language) (also known as Shqip) and English. We have sourced these datasets from Organization for Security and Co-operation in Europe (OSCE) website by applying appropriate language filters. Filtered list of documents in Albanian and Shqip can be found [here](https://www.osce.org/resources/documents?filters=%20sm_translations%3A%28sq%29&solrsort=score%20desc&rows=10).

The datasets can be found in the dataset directory. Each folder inside the dataset directory correspond to each document from the data was forced from. This directory contains the 3 text files and PDF files corresponding to the 3 languages. All the filenames start with a suffix corresponding to the language (en: English, mk: Macedonian, sh: Shqip).

While the PDF files are the original files found on the website, the text files contain *manually* extracted sentenced sentences from the PDF file.  Each text file has one sentence per line. Sentences across all the text files have a 1:1:1 mapping. Specifically, a sentence at line *n* in the English sentences' file, has a corresponding Macedonian and Shqip translation *at the same line* in the Macedonian and Shqip sentences' file.

For convenience, we have a concatenated all the sentences file into one bearing the document name. This contains the language identifier, URL to the document from which the sentences were extracted, and the sentences themselves.

# How to Contribute
You can contribute to Rosetta-Balcanica by following these instructions. For clarity, these instructions assume that you are extracting a document titled "North Macedonian Election Report" that is available in English, Shqip, and Macedonian. The instructions should work for any language combinations and documents.

1. Fork and clone the Rosetta Balcanica repo. Following instructions assume the root directory is rosetta-balcanica
2. Create a new directory within `dataset/english-macedonian-shqip/north_macedonian_election_report`. Appropriately create parent directories if they do not exist.
3. Save the original PDF files of the document corresponding to each language in the newly created directory. In this case we will have 3 PDF files: `english.pdf`, `shqip.pdf`, `macedonian.pdf`.
4. Manually extract the sentences from the PDF files and save them in text files corresponding to each language in the same directory. In this case we will have 3 text files: `english.txt`, `shqip.txt`, `macedonian.txt`.
5. Once the extractions are done, run the `data_setup.py` script passing in the languages directory: `src/data_setup.py dataset/english-macedonian-shqip`. This will aggregate all the files of all the documents in the languages directory, create training and testing split, zip them up and place them in the root directory. The resulting zip file will be named `rosetta_balcanica.tar.gz`
6. Add the new documents and the newly created zip file into the repo, commit, and push them.
7. Submit a pull request to have your contribution merged.

# Using Dataset

# Getting Dataset Statistics

## Testing 


