import streamlit as st
from PyPDF2 import PdfReader
from query import make_query
from chroma_db_script import generate_data_store

# Streamlit app title and description
st.markdown("""
# 📝 AI-Powered PDF Parser
All you need to do is:
1. Upload a PDF
2. Ask any questions about its contents
""")

file = st.file_uploader('📁 Upload your pdf format (max 100 pages)')
if file:
    st.write("File Uploaded")
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
else:
    st.write("Upload File")
with st.form('input_form'):
    submitted = st.form_submit_button("Submit PDF")

if submitted:
    txt_path = "data/text_data.txt"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

    generate_data_store()
    
    # with st.form('input_form2'):
    #     user_text = st.text_input("Ask your pdf anything:")
    #     submitted2 = st.form_submit_button()
    # print(submitted2)
    # print(user_text)
    # if submitted2:
    #     #question = input("Ask your pdf some question: ")
    #     print(user_text)
    #     rep = make_query(user_text)
    #     print(rep)
    #     st.write(rep)
    