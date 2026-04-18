---
title: ChatWithPDF RAG
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
---
## Live Demo

Try it here: https://aviralmonke-chatwithpdf.hf.space

# 📄 ChatWithPDF - RAG Application

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask context-aware questions using Large Language Models.

---

# Features

* Upload and process PDF documents
* Ask questions in natural language
* Context-aware responses using RAG
* Semantic search using vector embeddings
* Fast retrieval with FAISS

---

# Tech Stack

* **Frontend**: Streamlit
* **LLM Orchestration**: LangChain
* **Embeddings**: HuggingFace Embeddings
* **Vector Store**: FAISS
* **LLM Provider**: Groq / OpenAI
* **Other Tools**: Python, dotenv

---

# How It Works

1. PDF is uploaded and split into smaller chunks
2. Text chunks are converted into embeddings
3. Embeddings are stored in a FAISS vector database
4. User query is embedded and matched with relevant chunks
5. Relevant context is passed to the LLM
6. LLM generates an accurate, context-based response

---

# Setup Instructions

# 1. Clone the repository

```
git clone https://github.com/MishrA-Aviral/ChatwithPDF-RAG.git
cd ChatwithPDF-RAG
```

# 2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

# 3. Install dependencies

```
pip install -r requirements.txt
```

# 4. Add environment variables

Create a `.env` file and add your API key:

```
GROQ_API_KEY=your_api_key_here
```

(or OpenAI key if used)

# 5. Run the app

```
streamlit run app.py
```

---

# Future Improvements

* Support for multiple PDFs
* Chat history / conversational memory
* Better UI/UX
* Deployment (Streamlit Cloud / Render)

---

# Key Learnings

* Implemented a complete RAG pipeline
* Worked with vector databases (FAISS)
* Managed dependencies and reproducible environments
* Debugged real-world Git and deployment issues

---

# Contact

Feel free to connect or reach out for feedback!
