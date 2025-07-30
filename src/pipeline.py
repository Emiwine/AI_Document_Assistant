import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.generator import GroqGenerator

load_dotenv()

class RAGPipeline:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectorstore = FAISS.load_local('D:/Rag_CChatbot/Vectordb/Faiss_index', self.embeddings, allow_dangerous_deserialization=True)
        self.generator = GroqGenerator()
    
    def _smart_context_selection(self, context_chunks, max_tokens=2048):
        """Intelligently select chunks that fit within token limits"""
        selected_chunks = []
        current_tokens = 0
        
        for chunk in context_chunks:
            chunk_tokens = len(chunk) // 4
            
            if current_tokens + chunk_tokens < max_tokens:
                selected_chunks.append(chunk)
                current_tokens += chunk_tokens
            else:
                break
        
        return selected_chunks
    
    def stream_response(self, query, k=3):
        docs = self.vectorstore.similarity_search(query, k=k)
        context_chunks = [doc.page_content for doc in docs]
        selected_chunks = self._smart_context_selection(context_chunks)
        
      
        print(f"Retrieved {len(context_chunks)} chunks, using {len(selected_chunks)} chunks")       ### user can see that how many chunks is used 
        
  
        for token in self.generator.stream_response(selected_chunks, query):
            yield token
