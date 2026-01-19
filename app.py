import streamlit as st
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
import subprocess
import os
import sys


PDF_DIR = "data/pdfs"
DB_DIR = "vectordb"
os.makedirs(PDF_DIR, exist_ok=True)


st.set_page_config(page_title="PDF Q&A Assistant")

st.title("📄 Smart PDF Q&A Assistant")

st.markdown("### 1️⃣ Upload PDFs")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)
if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(PDF_DIR, file.name), "wb") as f:
            f.write(file.getbuffer())

    st.success("PDFs uploaded successfully!")





# ------------------ INGEST BUTTON ------------------
st.markdown("### 2️⃣ Create Embeddings")

if st.button("Create Embeddings"):
    with st.spinner("Running ingestion pipeline..."):
        try:
            result = subprocess.run(
                [sys.executable, "ingest.py"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                st.success("Embeddings created successfully!")
            else:
                st.error("Ingestion failed")
                st.code(result.stderr)

        except Exception as e:
            st.error(f"Error running ingest.py: {e}")

st.divider()



embeddings = OllamaEmbeddings(model="nomic-embed-text")
db = Chroma(persist_directory="vectordb", embedding_function=embeddings)

llm = ChatOllama(model="gpt-oss:20b-cloud")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

query = st.text_input("Ask a question from your PDFs:")

if query:
    with st.spinner("Thinking..."):
        response = qa_chain.invoke(query)

    st.subheader("Answer")
    st.write(response["result"])





