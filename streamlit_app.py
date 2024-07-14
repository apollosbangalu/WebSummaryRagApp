import streamlit as st
import os
from dotenv import load_dotenv
from document_loader import load_webpage
from text_splitter import split_text
from vector_store import create_vector_store
from retriever import get_retriever
from qa_chain import create_qa_chain

# Load environment variables
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

st.title("Webpage Q&A App")

# Input for webpage URL
url = st.text_input("Enter the URL of the webpage:")

if url:
    with st.spinner("Loading and processing the webpage..."):
        # Load webpage
        document = load_webpage(url)

        # Split the document into chunks
        splits = split_text(document)

        # Create vector store
        vector_store = create_vector_store(splits)

        # Get retriever
        retriever = get_retriever(vector_store)

        # Create QA chain
        qa_chain = create_qa_chain(retriever)

    st.success(f"Successfully loaded and processed the webpage: {url}")

    # Question input
    question = st.text_input("Enter your question:")

    if question:
        with st.spinner("Generating answer..."):
            # Get answer
            response = qa_chain.invoke({"input": question})
            st.write(f"Answer: {response['answer']}")
