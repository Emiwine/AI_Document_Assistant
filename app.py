import streamlit as st
import os
from src.pipeline import RAGPipeline
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(    ### page taskbar heading 
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pipeline" not in st.session_state:
    try:
        st.session_state.pipeline = RAGPipeline()
    except Exception as e:
        st.error(f"Error initializing RAG pipeline: {str(e)}")
        st.stop()



### App heading for this project 

st.title("AI Document Assistant ")
st.markdown("Ask questions about your documents and get AI-powered responses!")


with st.sidebar:
    st.header("Settings")
    
    k_chunks = st.slider("Number of chunks to retrieve", 1, 100,30)   ## number of chunks that have to retrive 
    
    if st.button("Clear Chat History"):     ## remove the chat history
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("**Powered by:**")
    st.markdown("- 🔍 FAISS Vector Store")
    st.markdown("- ⚡ Groq API (Gemma2-9b-It)")
    st.markdown("- 🚀 Streamlit")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



### Chat input prompt 

if prompt := st.chat_input("Ask a question about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            for token in st.session_state.pipeline.stream_response(prompt, k=k_chunks):
                full_response += token
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            error_message = f"Sorry, I encountered an error: {str(e)}"
            message_placeholder.markdown(error_message)
            full_response = error_message
    

    st.session_state.messages.append({"role": "assistant", "content": full_response})


st.markdown("---")
st.markdown("💡 **Tip:** Ask specific questions about your documents for better results!")
