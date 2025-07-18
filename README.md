# 🤖 Agentic RAG System

This project demonstrates a production-ready Retrieval-Augmented Generation (RAG) system with agentic orchestration, powered by LangChain, OpenAI, and FAISS. It supports both interactive demos (via Streamlit) and API integration (via FastAPI), with optional WhatsApp support using Twilio.

---

## 🚀 Features

- 🔍 **Document-aware RAG**: Uses OpenAI embeddings + FAISS
- 🧠 **Agentic Orchestration**: Modular tool use with LangChain agents
- 🌍 **Multilingual Fallback**: Clarifies questions via LLM
- 🧪 **Testing Ready**: Includes unit tests for core pipeline
- 📲 **WhatsApp Integration**: Send questions via WhatsApp using Twilio
- 🖥️ **Streamlit UI**: For live question-answering demos
- 🔌 **FastAPI Server**: For backend / bot integrations

---

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Setup

Create a `.env` file:
```
OPENAI_API_KEY=your_openai_key
WEATHER_API_KEY=your_openweather_key
```

---

## 🧠 Run the Ingestion Pipeline

```bash
python -m app.ingestion
```

---

## 📚 Query with RAG

```bash
python -m app.rag_pipeline
```

---

## 💬 Run the Agentic Tool-Orchestrator

```bash
python -m app.agentic_orchestrator
```

---

## 🧪 Run Tests

```bash
python -m unittest tests/test_rag.py
```

---

## 🌐 Run FastAPI

```bash
uvicorn api_main:app --reload --port 8001
```

### 📩 Optional: Enable WhatsApp Webhook (Twilio)

```bash
python3 twilio_webhook.py
# Expose with ngrok:
ngrok http 8002
```

Set your Twilio webhook to:
```
https://your-ngrok-url.ngrok.io/twilio
```

---

## 🖼️ Run the Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🗂️ Project Structure

```
├── app/
│   ├── ingestion.py
│   ├── rag_pipeline.py
│   ├── agentic_orchestrator.py
│   ├── fallback_handler.py
│
├── tools/
│   ├── tool_calculator.py
│   ├── tool_weather.py
│
├── tests/
│   └── test_rag.py
│
├── api_main.py            # FastAPI server
├── streamlit_app.py       # Streamlit interface
├── twilio_webhook.py      # Twilio integration endpoint
├── requirements.txt
├── docker-compose.yml
├── README.md
```

---

## 👤 Author

Victor Fernando — built for demonstrating production-grade AI agent skills with LangChain + OpenAI + Twilio.

