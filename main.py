from query import make_query
from chroma_db_script import generate_data_store
from dataloaders import load_pdf
from retrievers import similarity_search, reciprocal_rank_fusion

load_pdf(False)
generate_data_store()
start = "y"
while start == "y":
    question = input("Ask your pdf some question: ")
    #print(make_query(question))
    print(similarity_search(question))
    #print(reciprocal_rank_fusion(question))
    start = input("Would you like to keep chatting: ")
    