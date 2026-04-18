import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import os 
import tempfile
from dotenv import load_dotenv
load_dotenv()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "retriever" not in st.session_state:
    st.session_state.retriever = None

st.set_page_config(page_title="Chat With PDF", page_icon="😝")
st.title("📄Chat with your PDF")



with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("choose a PDF file", type=["pdf"])

if uploaded_file and st.session_state.retriever is None:
    with st.spinner("Processing PDF..."):
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            f.write(uploaded_file.read())
            temp_path = f.name

        
        loader = PyPDFLoader(temp_path)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = splitter.split_documents(docs)

       
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(splits, embeddings)
        st.session_state.retriever = vectorstore.as_retriever()

        os.unlink(temp_path)
    st.success("PDF processed! Ask me anything.")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if query := st.chat_input("Ask a question about your PDF..."):
    if st.session_state.retriever is None:
        st.warning("Please upload a PDF first!")
    else:
        st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            docs = st.session_state.retriever.invoke(query)
            context = "\n\n".join(doc.page_content for doc in docs)
            response = llm.invoke(f"Answer based on this context:{context}\n\nQuestion: {query}")
            st.write(response.content)
            st.session_state.messages.append({"role": "assistant", "content": response.content})

