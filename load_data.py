from PyPDF2 import PdfReader

def pdf_to_text():
    print("Enter path of single pdf, or comma seperated list of paths\n")
    paths = input().split(',')
    for path in paths:
        file = open(path, 'rb')
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        txt_path = f"data/{path.split('/')[-1]}_01.txt"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Document converted to text")
