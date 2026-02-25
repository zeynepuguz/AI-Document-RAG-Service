from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load the document
loader = TextLoader('data/my_document.txt')
documents = loader.load()

# Split the document into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
document_chunks = splitter.split_documents(documents)

# Initialize embeddings with OpenAI API key
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# FAISS expects document objects and the embedding model
vector_store = FAISS.from_documents(document_chunks, embeddings)

# Use the vector store's retriever
retriever = vector_store.as_retriever()

# Initialize the LLM (using OpenAI)
llm = OpenAI(openai_api_key=openai_api_key)

# Set up the retrieval-based QA chain
qa_chain = RetrievalQA.from_chain_type(
   llm=llm,
   chain_type="stuff",
   retriever=retriever
)

# Example query
query = "Are polar bears in danger?"
response = qa_chain.invoke({"query": query})

# Print the response
print(response)