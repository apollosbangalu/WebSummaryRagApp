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

# Set page config
st.set_page_config(page_title="Webpage Q&A App", page_icon="🌐", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        color: #ffffff;
        background-color: #4B0082;
        border-radius: 20px;
        border: 2px solid #8A2BE2;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #8A2BE2;
        border-color: #4B0082;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #4169E1;
    }
    .stAlert {
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌐 Webpage Q&A App</h1>", unsafe_allow_html=True)

# App summary
st.markdown("""
### How to use this app:
1. Enter the URL of a webpage you want to ask questions about.
2. Wait for the app to process the webpage.
3. Once processed, enter your question about the webpage content.
4. Click the 'Get Answer' button to receive an AI-generated answer based on the webpage content.
""")

# Input for webpage URL
url = st.text_input("🔗 Enter the URL of the webpage:", key="url_input")

if url:
    with st.spinner("🔍 Loading and processing the webpage..."):
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

    st.success(f"✅ Successfully loaded and processed the webpage: {url}")

    # Question input
    question = st.text_input("❓ Enter your question:", key="question_input")

    if question:
        if st.button("🔮 Get Answer", key="answer_button"):
            with st.spinner("🧠 Generating answer..."):
                # Get answer
                response = qa_chain.invoke({"input": question})
                st.markdown(f"**Answer:** {response['answer']}")

# Add a footer
st.markdown("""
<div style='position: fixed; bottom: 0; left: 0; right: 0; background-color: #4B0082; color: white; text-align: center; padding: 10px;'>
    Made with ❤️ and Streamlit
</div>
""", unsafe_allow_html=True)
