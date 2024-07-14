from langchain_community.document_loaders import WebBaseLoader

def load_webpage(url):
    """
    Load a webpage and return the document.
    """
    loader = WebBaseLoader(web_paths=[url])
    documents = loader.load()
    return documents[0]
