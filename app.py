import streamlit as st
from PyPDF2 import PdfReader
from vector_storage import generate_data_store
from dataloaders import load_pdf
from retrievers import *

# Streamlit app title and description
st.markdown("""
# 📝 Chat with your PDF using AI!
All you need to do is:
1. Upload a PDF
2. Ask any questions about its contents
""")

file = st.file_uploader('📁 Upload your pdf format (max 100 pages)')
if file:
    st.write("File Uploaded")
else:
    st.write("Upload File")

with st.form('input_form'):
    submitted = st.form_submit_button("Submit PDF")
    if submitted:
        load_pdf(file)
        generate_data_store()
    
with st.form('input_form2'):
    user_text = st.text_input("Ask your pdf anything:")
    submitted2 = st.form_submit_button()
    if submitted2:
        print(user_text)
        rep = reciprocal_rank_fusion(user_text)
        print(rep)
        st.write(rep)
    