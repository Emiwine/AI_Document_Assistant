import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class GroqGenerator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "Gemma2-9b-It"               # i used this model 
    
    def generate_response(self, context_chunks, query):
        context = "\n".join(context_chunks)
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer based on the context:"
        
        response = self.client.chat.completions.create(   ## generate responsess
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            temperature=0.3,
            max_tokens=2048
        )
        
        return response.choices[0].message.content
    
    def stream_response(self, context_chunks, query):
        context = "\n".join(context_chunks)
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer based on the context:"
        
        stream = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            temperature=0.3,
            max_tokens=1024,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
