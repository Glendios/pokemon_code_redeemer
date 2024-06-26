import fitz #pymupdf
import os
import sys
from textenterer import click_paste_10

def txtParser(name):
    codelist = []
    try:
        with open(name, 'r', encoding='utf-8') as file:
            text = file.read() 
        text = text.replace('-','')
        delimited_text = text.replace('\n', ' ').split()
        print(text)
        print(delimited_text)
        for line in delimited_text:
            #print(len(line))
            if len(line) > 12:
                if len(line) < 17:
                    codelist.append(line)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(f"Failed to open file.")
    return codelist
    #pass

def pdfParser(name):
    codelist = []
    try:
        pdf_document = fitz.open(name)
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text = page.get_text()
            text = text.replace('-','')
            delimited_text = text.replace('\n', ' ').split()
            print(text)
            print(delimited_text)
            for line in delimited_text:
                #print(len(line))
                if len(line) > 12:
                    if len(line) < 17:
                        codelist.append(line)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(f"Failed to open file.")
    print(codelist)
    return codelist
    #pass

def directCodes(manual_list):
    text = manual_list
    codelist = []
    delimited_text = text.replace('\n', ' ').split()
    print(text)
    print(delimited_text)
    for line in delimited_text:
        #print(len(line))
        if len(line) > 12:
            if len(line) < 17:
                codelist.append(line)
    return codelist
    pass


#main function
if len(sys.argv) > 1:
    pdf_name = sys.argv[1]
else:
    pdf_name = input("Please enter filename (include .txt/.pdf extension), or directly enter codes:")
    abs_dir = os.path.dirname(os.path.abspath(__file__))
    print(abs_dir)
    #current_dir = os.getcwd()
    #full_path = os.path.join(current_dir, pdf_name)
    full_path = os.path.join(abs_dir, pdf_name)
    print(full_path)
    if pdf_name.endswith(".txt"):
        if os.path.isfile(full_path):
            codelist = txtParser(full_path)
        else:
            print("File not found")
        pass
    elif pdf_name.endswith(".pdf"):
        #if os.path.isfile(full_path):
        if os.path.isfile(full_path):
            codelist = pdfParser(full_path)
        else:
            print("File not found")
        pass
    else:
        codelist = directCodes(pdf_name)
start_index_str = input("Enter which code to start at (integer) or nothing if 0: ").strip()
start_index = int(start_index_str) if start_index_str else 0
click_paste_10(codelist, 10, start_index)