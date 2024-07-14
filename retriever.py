def get_retriever(vector_store):
    """
    Get a retriever from the vector store.
    """
    return vector_store.as_retriever(search_kwargs={"k": 3})
