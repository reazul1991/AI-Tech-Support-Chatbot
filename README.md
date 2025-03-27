# AI Tech Support Chatbot

This is a custom GPT-4-powered AI chatbot built with **LangChain**, **Streamlit**, and **FAISS**, designed to answer questions about historical technical support tickets.

It allows users to ask detailed, follow-up questions about ticket topics, resolutions, SLAs, assigned agents, and more — just like a real customer support expert.

---

## Features

- Conversational Retrieval (QA over support ticket data)
- Memory-enabled follow-up questions
- Vectorized ticket data using OpenAI Embeddings + FAISS
- Powered by GPT-4 via LangChain's ChatOpenAI
- Secure API key management using `.env`
- Streamlit-based frontend (chat UI)

---

## Project Structure

```
AI-Tech-Support-Chatbot
🔹 app.py
🔹 .env                # (excluded from GitHub)
🔹 .gitignore
🔹 requirements.txt
🔹 tech_support_qa.json
🔹 ticket_support_db/  # (excluded from GitHub)
```

---

## Installation

```bash
git clone https://github.com/reazul1991/AI-Tech-Support-Chatbot.git
cd AI-Tech-Support-Chatbot
pip install -r requirements.txt
```

---

## Set Up Your `.env` File

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## How It Works

1. Vectorizes Q&A data from your support ticket dataset
2. Stores vectors using FAISS
3. User inputs a natural language query
4. Relevant ticket chunks are retrieved
5. GPT-4 generates a contextual answer
6. Chat history is preserved using LangChain Memory

---

## Run Locally

```bash
"streamlit run app.py" or "python -m streamlit run app.py"
```

Open the browser URL that appears (typically `http://localhost:8501`).

---

## Example Questions to Ask

- What happened with the ticket about product setup?
- Who handled the password reset ticket?
- Was the SLA met for email configuration?
- Which agent resolved issues related to the software install?

---

## Demo (Optional)

_(Coming soon)_

---

## Tech Stack

- Python 3.11
- Streamlit
- LangChain
- OpenAI (GPT-4 + Embeddings)
- FAISS
- dotenv

---

## Contact

If you'd like to hire me for an AI/ML or chatbot project, feel free to reach out via:

- Email: reaz.pfec@gmail.com
- GitHub: [@reazul1991](https://github.com/reazul1991)

---

## License

MIT License
