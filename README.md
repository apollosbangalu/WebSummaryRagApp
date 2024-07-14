# Webpage Q&A App

## Description

The Webpage Q&A App is an interactive tool that allows users to ask questions about the content of any webpage. It uses advanced natural language processing and machine learning techniques to provide accurate answers based on the webpage's content.

## Main Technologies and Components

- **Python**: The primary programming language used for the application.
- **Streamlit**: Used for creating the web-based user interface.
- **LangChain**: Provides the framework for building the question-answering system.
- **OpenAI's GPT-4**: Powers the natural language understanding and generation.
- **Chroma**: Used as the vector store for efficient similarity search.

Key components of the application include:

1. **Document Loader**: Fetches and loads the content of the specified webpage.
2. **Text Splitter**: Breaks down the webpage content into manageable chunks.
3. **Vector Store**: Stores and indexes the text chunks for efficient retrieval.
4. **Retriever**: Fetches relevant text chunks based on the user's question.
5. **QA Chain**: Combines the retrieved information with the language model to generate answers.

## How to Run the App

1. Clone this repository to your local machine.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

4. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

5. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## How to Use the App

1. Enter the URL of the webpage you want to ask questions about in the provided input field.

2. Wait for the app to process the webpage. This may take a few moments depending on the size of the webpage.

3. Once the webpage is processed, you'll see a success message.

4. Enter your question about the webpage content in the question input field.

5. Click the "Get Answer" button to receive an AI-generated answer based on the webpage content.

6. You can ask multiple questions about the same webpage or load a new webpage by entering a new URL.

## Note

This application requires an active internet connection to fetch webpage content and communicate with the OpenAI API. Ensure you have a stable internet connection while using the app.

## License

This project is open-source and available under the MIT License.
