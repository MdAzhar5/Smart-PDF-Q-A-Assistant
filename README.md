# 📄 Smart PDF Q&A Assistant

A simple tool that lets you **ask questions from your PDFs** and get **answers instantly**.  
Upload your PDFs and start learning!

---

## 🔹 Features

- Upload **one or more PDFs**  
- **Create embeddings** (process PDFs to understand them)  
- Ask questions and get **answers from your PDFs**  
- See **which PDF and page** the answer came from  

---

## ⚙️ How It Works

1. Upload PDFs  
2. Click **"Create Embeddings"** to process your PDFs  
3. Ask a question in the box  
4. Get the **answer** and **source PDF & page number**  

We use **LangChain** and a **local AI model (Ollama)** to understand your PDFs.

---

## 💻 Requirements

- Python 3.10+  
- Virtual environment (optional but recommended)  
- Install dependencies:
🚀 How to Use

Upload PDFs: Drop your PDFs in the app

Create Embeddings: Click the button to prepare your PDFs

Ask Questions: Type any question about your PDFs

Example questions:

"What is the main idea of chapter 2?"

"Explain this concept in simple words."

📁 Project Structure
Smart-PDF-Q-A-Assistant/
│
├── app.py          # Main Streamlit app
├── ingest.py       # Processes PDFs and creates embeddings
├── data/pdfs/      # Put your PDF files here
├── vectordb/       # Vector database for embeddings
├── requirements.txt
└── README.md

✅ Notes

Make sure Python packages are installed in the same environment as Streamlit

Run Streamlit like this:

streamlit run app.py


PDFs stay local — nothing is uploaded online
```bash
pip install -r requirements.txt
