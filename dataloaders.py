from PyPDF2 import PdfReader
import os
from langchain.docstore.document import Document
from langchain.indexes import VectorstoreIndexCreator

def load_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    txt_path = "data\\user_data.txt"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    f.close()
    print("Document converted to text")

def load_local_pdf(user:bool):
    if user:
        print("Enter path of single pdf, or comma seperated list of paths\n")
        paths = input().split(',')
    else:
        paths = ["C:\\Users\\shahn\\Documents\\GitHub\\noob-rag\\raw_data\\README.pdf"]
    for count, path in enumerate(paths):
        file = open(path, 'rb')
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        txt_path = f"data\data{count}.txt"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        f.close()
        print("Document converted to text")
            
