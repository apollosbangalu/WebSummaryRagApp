import os
from dotenv import load_dotenv
from document_loader import load_webpage
from text_splitter import split_text
from vector_store import create_vector_store
from retriever import get_retriever
from qa_chain import create_qa_chain

def main():
    # Load environment variables
    load_dotenv()

    # Get OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    # Main application loop
    while True:
        # Get webpage URL from user
        url = input("Enter the URL of the webpage: ")

        # Load webpage
        document = load_webpage(url)

        # Print the contents of the page
        print("Webpage contents:")
        print(document.page_content)

        # Ask if user wants to continue
        continue_input = input("Do you want to load another webpage? (y/n) ")
        if continue_input.lower() != "y":
            break

if __name__ == "__main__":
    main()
