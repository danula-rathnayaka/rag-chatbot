# 🤖 FAQ RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Python, LangChain, ChromaDB, and Streamlit. The chatbot
answers user questions by retrieving relevant information from a knowledge base (FAQs) and generating contextual
responses using a language model.

---

## Features

- **Retrieval-Augmented Generation**: Combines vector search with LLM-powered answer generation.
- **FAQ Knowledge Base**: Load, query, and expand a CSV-based FAQ dataset.
- **Streamlit Web App**: User-friendly interface for asking questions and managing FAQs.
- **Persistent Storage**: All Q&A interactions can be logged to a text file.
- **Easy Extensibility**: Add new FAQs or adapt to other datasets with minimal code changes.

---

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/yourusername/faq-rag-chatbot.git
cd faq-rag-chatbot
```

### 2. Install Dependencies

It is recommended to use Python 3.12+. Install dependencies with:

```
pip install -r requirements.txt
```

### 3. Prepare the FAQ Dataset

- Place your `faqs.csv` file in the `resources/` directory.
- The CSV should have columns: `question` and `answer`.

### 4. Run the App

```
streamlit run main.py
```

Open your browser at [http://localhost:8501](http://localhost:8501).

---

## Usage

- **Ask Questions**: Enter a question in the app. The chatbot retrieves relevant FAQs and generates an answer.
- **View Knowledge Base**: See all current FAQs in the app.
- **Add New FAQs**: Use the form to add new question-answer pairs.
- **Q&A Logging**: All interactions are saved in `outputs/qa_log.txt`.

---

## Deployment

You can deploy this app using Docker:

```
docker build -t faq-rag-chatbot .
docker run -p 8501:8501 faq-rag-chatbot
```

Or deploy to [Streamlit Community Cloud](https://streamlit.io/cloud).

---

## Citations & Resources

- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Perplexity AI](https://www.perplexity.ai/)

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, contact [danusathmin@gmail.com](mailto:danusathmin@gmail.com).
