from vector_storage import generate_data_store
from dataloaders import load_pdf
from retrievers import *

load_pdf(False)
generate_data_store()
start = "y"
while start == "y":
    question = input("Ask your pdf some question: ")
    print(reciprocal_rank_fusion(question))
    start = input("Would you like to keep chatting: ")
    