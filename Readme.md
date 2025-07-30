
# 🤖 RAG Chatbot: Document-Based Q&A System

---

## 📄 Overview

This project is a smart chatbot that answers user queries based only on a specific PDF document (like Terms & Conditions).  
It uses **Retrieval-Augmented Generation (RAG)**, combining semantic search (via embeddings and FAISS vector database) with a large language model (LLM) to deliver accurate, transparent, and grounded answers through a real-time Streamlit web interface.

---

## ✨ Features

- 📑 **Document-grounded Q&A:** Answers come strictly from your uploaded document(s), no outside data.
- 🧠 **Semantic search:** Uses pre-trained embeddings (e.g., all-MiniLM-L6-v2) and a vector database (FAISS) for highly relevant text retrieval.
- 🤝 **LLM-powered generation:** Utilizes models like Gemma, Mistral, or Llama (via Groq API) to generate natural, context-aware responses.
- ⚡ **Real-time chat:** Streamlit web app streams responses as they are generated, for a conversational, interactive experience.
- 🔍 **Transparency:** Highlights which chunks of the document were used for each answer.

---

## 🗂️ Project Structure

```
├── data_cleaning.ipynb       # 🧹 Cleans and chunks the PDF document text
├── embedding.ipynb           # 🧬 Converts text chunks to vector embeddings and builds vector DB (FAISS)
├── generator.py              # 🤖 Connects to LLM (via Groq) for grounded answer generation
├── pipeline.py               # 🔗 Runs retrieval, prompt construction, and answer generation pipeline
├── app.py                    # 💬 Streamlit app with live chat UI
└── AI_Training_Document.pdf  # 📄 Example PDF document (upload your own as needed)
```

---

## 🔬 How It Works (Deep Dive)

1. ✂️ **Chunking:** Splits PDF into small, language-aware segments for fine-grained retrieval.
2. 🧬 **Embedding:** Uses transformer models to convert each chunk into a high-dimensional vector representing its meaning.
3. 📦 **Indexing:** Embedding vectors are stored in FAISS for fast similarity search.
4. 🔍 **Retrieval:** On user query, the system computes the query’s embedding and retrieves the k-most relevant chunks from FAISS.
5. 📝 **Prompt Construction:** Gathers the query and retrieved chunks into a formatted prompt template.
6. 🤖 **LLM Generation:** Sends the prompt to the selected LLM API; answer is generated ‘grounded’ in the retrieved evidence only.
7. 💬 **UI:** Streams answer to web chat, highlighting which document chunks were referenced for maximum transparency.

---

## 🧩 Example Usage

**User:** “What penalties are there for late payment?”
- 📄 The app finds related regulations in your document, sends them to the LLM, and immediately streams an answer—**citing the exact paragraphs used.**

---

## 📈 Extending & Customizing

- 🗃️ **Support for multi-PDF corpora:** Track documents and chunk sources, concatenate multiple embeddings, or shard by document domain.
- 🔄 **Swap LLM APIs:** Abstract the `generator.py` logic to use OpenAI, Anthropic, or local LLMs.
- ⚙️ **Embed better:** Swap out embedding models for domain-tuned ones.
- 🧩 **Improve prompt engineering:** Modify the template for greater control or to add citation formatting.
- 💎 **Frontend tweaks:** Refine Streamlit’s UI/UX or migrate to React for more features.

---

## 🛡️ Security & Privacy

- 🔒 All documents and chats stay on your own infrastructure.
- 🔐 (Optional) Add user authentication or data redaction per organization policy.

---

## 🧪 Testing & Evaluation

- 📝 Includes sample queries in `tests/` (add as needed).
- 📊 Use retrieval and answer correctness metrics (accuracy, recall, response groundedness).
- 🧩 Add end-to-end integration tests with Streamlit’s testing tools.

---

## 📚 Dependencies

- 🐍 python >= 3.9
- 🎈 streamlit
- 🧬 sentence-transformers
- 📦 faiss-cpu
- 📄 pypdf / pdfplumber
- 🌐 requests
- (plus LLM API dependencies, e.g., groq, openai)

---