from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(document):
    """
    Split the document into chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents([document])
