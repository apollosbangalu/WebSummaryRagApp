from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def create_qa_chain(retriever):
    """
    Create a question-answering chain.
    """
    llm = ChatOpenAI(model="gpt-4")

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    Context: {context}

    Question: {input}

    Answer: """)

    document_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever, document_chain)
