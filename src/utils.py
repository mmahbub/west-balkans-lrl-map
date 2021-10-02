import pdfplumber
import re

def extract_text(pdf_file):
    """
    Extract TEXT from PDF - page by page
    
    input:  PDF file
    output: A list of extracted text. Each list element is a page.
            
    """
    text=[]
    with pdfplumber.open(pdf_file) as pdf:
        pages = pdf.pages
        for i,pg in enumerate(pages):
            txt = pages[i].extract_text()
            text.append(txt)
    return text

def remove_footnotes(raw_text, pgStart, pgEnd, 
                     UNTIL_END=True,CHECK_OUTPUT=False):
    """
    Use regex to remove footnotes
    
    input:  List of raw extracted page
    output: List of extracted page with no footnotes
    
    """
    # 1. We need pgEnd because some documents has no text 
    # at the end and so `extract_text` returns None.
    # 2. We need pgStart because sometimes the same article 
    # written in 2 different languages have different 
    # "Acronyms and Abbreviations" and so it creates 
    # wrong 1:1 mapping
    
    text_nofoot = []
    
    if UNTIL_END:
        text = raw_text[pgStart:]
    else:
        text = raw_text[pgStart:pgEnd]
        
    for i in range(len(text)):
        print(f'\nPage Number: {i}')
        
        exp1 = r"\n                                                                                                                                                                                           \n"
        exp2 = r"\n                                                 \n\d"
        exp3 = r"\n                                                           \n\d"
        idxs = re.findall(exp1,text[i]) + re.findall(exp2,text[i]) + re.findall(exp3,text[i])
        
        if idxs:
            text_f = text[i][:text[i].find(idxs[0])]
            
            if CHECK_OUTPUT:
                print(f'\nRemoved Footenotes: {text[i][text[i].find(idxs[0]):]}')
                print('\n--------------------------NEW PAGE----------------------------\n')
                
        else:
            text_f = text[i]
        text_nofoot.append(text_f)
            
    return text_nofoot
