# 🤖 Gemini AI Chatbot (Streamlit)

A modern **Generative AI chatbot** built using **Google Gemini**, featuring a **ChatGPT-like UI**, **multi-session chat history**, and **LLMOps monitoring with LangSmith**.  
Designed to demonstrate **real-world LLM integration, prompt engineering, and production-ready UI design**.

---

## 🚀 Features

- 🔹 Gemini-powered conversational AI  
- 🔹 Chat-style interface using Streamlit  
- 🔹 Multiple chat sessions with history (Today / Older)  
- 🔹 Session-based conversation titles  
- 🔹 Prompt engineering using LangChain  
- 🔹 LLMOps integration with **LangSmith** (tracing & debugging)  
- 🔹 Secure environment variable handling  
- 🔹 Clean, responsive UI with custom CSS  

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Web UI  
- **Google Gemini API** (`gemini-2.5-flash`)  
- **LangChain**
- **LangSmith (LLMOps)**
- **Prompt Engineering**

---

## 📂 Project Structure

```
├── app.py
├── README.md
---


```
GOOGLE_API_KEY=your_google_gemini_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=My-GenAI-Project-Gemini
```


###  Run the application
```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a query in the chat UI  
2. Prompt template formats the query  
3. Request is sent to **Google Gemini**  
4. Response is parsed and displayed  
5. Chat history stored using Streamlit session state  
6. LangSmith tracks LLM calls and performance  

---

## ⚠️ Challenges & Learnings

- Understanding Gemini response behavior  
- Managing multi-session chat state  
- Prompt tuning for consistency  
- Debugging LLM calls using LangSmith  
- Building a scalable chat UI  

---

## 📌 Future Improvements

- Conversation memory  
- Authentication  
- RAG-based document chat  
- Cloud deployment  
- Multi-model support  

---

## 👤 Author

**Tarun Kumar Rathore**  
LinkedIn: https://www.linkedin.com/in/tarun-kumar-rathore-3012a4246/
GitHub: https://github.com/Tarungolu422

---

⭐ If you like this project, feel free to star the repository!
