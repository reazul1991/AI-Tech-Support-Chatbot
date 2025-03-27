import os
import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load FAISS vector store
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
db = FAISS.load_local("ticket_support_db", embeddings=embedding, allow_dangerous_deserialization=True)

# Initialize GPT-4 LLM
llm = ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=openai_api_key)

# Memory setup
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"
)

# Build the chatbot chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    memory=memory,
    return_source_documents=True,
    output_key="answer"
)

# Streamlit UI
st.set_page_config(page_title="AI Support Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 AI Support Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question about a support ticket:")

if user_input:
    response = qa_chain({"question": user_input})
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response["answer"]))

for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")
