import streamlit as st
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

st.set_page_config(page_title="PDF Q&A Assistant")

st.title("📄 Smart PDF Q&A Assistant")

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
        response = qa_chain(query)

    st.subheader("Answer")
    st.write(response["result"])

    st.subheader("Sources")
    for doc in response["source_documents"]:
        st.write(f"- Page {doc.metadata.get('page', 'N/A')}")
