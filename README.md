# AI Document RAG Service 🚀  
### LangChain + FastAPI + OpenAI

A simple **Retrieval-Augmented Generation (RAG)** API built using **LangChain**, **OpenAI**, and **FastAPI**.

This project demonstrates how to:
- Load and process documents
- Split documents into chunks
- Generate embeddings
- Build a vector store
- Retrieve relevant context
- Generate answers using an LLM
- Expose everything through a FastAPI endpoint

---

## 📌 Features

- 📄 Document loading from `data/`
- ✂️ Chunking with `RecursiveCharacterTextSplitter`
- 🔢 OpenAI Embeddings
- 🗄 Vector Store (FAISS / Chroma)
- 🔍 Similarity-based retrieval (Top-K)
- ⚡ FastAPI REST endpoint
- 📚 Swagger UI documentation

---

## 📁 Project Structure


AI-Document-RAG-Service/
│
├── data/
│ └── my_document.txt
│
├── assets/
│ └── image.png
│
├── rag.py
├── endpoints.py
├── main.py
├── requirements.txt
├── .gitignore
└── .env (NOT committed)


---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-Document-RAG-Service.git
cd AI-Document-RAG-Service
2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Create .env file

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here

⚠️ Do NOT commit .env to GitHub.

▶️ Run the API
uvicorn main:app --reload

Open in your browser:

http://127.0.0.1:8000/docs

Swagger UI will appear.

🔎 Query Example

Endpoint:

GET /query/?query=Are polar bears in danger?

Example curl request:

curl "http://127.0.0.1:8000/query/?query=Are%20polar%20bears%20in%20danger%3F"
