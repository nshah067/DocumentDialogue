from query import make_query
from chroma_db_script import generate_data_store
from load_data import pdf_to_text

pdf_to_text()
generate_data_store()
start = "y"
while start == "y":
    question = input("Ask your pdf some question: ")
    print(make_query(question))
    input("Would you like to keep chatting: ")
    