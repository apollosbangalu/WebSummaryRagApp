from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_store(splits):
    """
    Create a vector store from the text splits.
    """
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(splits, embeddings)
    return vector_store
