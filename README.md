# Dataset for Low Resource West Balkan Languages

As of now, we have dataset for two West Balkan languages [Macedonian](https://en.wikipedia.org/wiki/Macedonian_language) and [Albanian](https://en.wikipedia.org/wiki/Albanian_language) (also known as Shqip) and English. We have sourced these datasets from Organization for Security and Co-operation in Europe (OSCE) website by applying appropriate language filters. Filtered list of documents in Albanian and Shqip can be found [here](https://www.osce.org/resources/documents?filters=%20sm_translations%3A%28sq%29&solrsort=score%20desc&rows=10).

The datasets can be found in the dataset directory. Each folder inside the dataset directory correspond to each document from the data was forced from. This directory contains the 3 text files and PDF files corresponding to the 3 languages. All the filenames start with a suffix corresponding to the language (en: English, mk: Macedonian, sh: Shqip).

While the PDF files are the original files found on the website, the text files contain *manually* extracted sentenced sentences from the PDF file.  Each text file has one sentence per line. Sentences across all the text files have a 1:1:1 mapping. Specifically, a sentence at line *n* in the English sentences' file, has a corresponding Macedonian and Shqip translation *at the same line* in the Macedonian and Shqip sentences' file.

For convenience, we have a concatenated all the sentences file into one bearing the document name. This contains the language identifier, URL to the document from which the sentences were extracted, and the sentences themselves.

# Introduction

# Background

# Resources

