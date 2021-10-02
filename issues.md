### Issue 1:
    * Python extracts PDFs page by page
    * Articles written in different languages have different footnotes
    * This creates an issue when we try to create 1:1 mapping between documents
    * So we need a module that can remove footnotes from the documents right after we extract text from the documents
    * Module `remove_footnotes` inside `utils.py` serves that purpose
