import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
import streamlit as st

# ─────────────────────────────────────────
# API Key Setup
# ─────────────────────────────────────────
load_dotenv()

# ─────────────────────────────────────────
# LLM Setup
# ─────────────────────────────────────────
llm =  ChatGroq(model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500
)

# ─────────────────────────────────────────
# System Prompt
# ─────────────────────────────────────────
SYSTEM_PROMPT = """
You are a friendly and knowledgeable health assistant.
Your role is to answer general health-related questions in a clear,
simple, and supportive manner.

Important rules:
- Always be friendly, calm, and empathetic
- Give general health information only
- NEVER diagnose diseases or prescribe medications
- For serious symptoms always say: "Please consult a doctor immediately"
- For mental health issues always say: "Please speak to a mental health professional"
- Keep responses concise and easy to understand
"""

# ─────────────────────────────────────────
# Prompt Template
# ─────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# ─────────────────────────────────────────
# Safety Filter
# ─────────────────────────────────────────
def safety_filter(query):
    dangerous_keywords = [
        "suicide", "kill myself", "overdose",
        "self harm", "how to die", "end my life"
    ]
    for keyword in dangerous_keywords:
        if keyword.lower() in query.lower():
            return True
    return False

# ─────────────────────────────────────────
# Get Response
# ─────────────────────────────────────────
def get_response(user_input, chat_history):
    if safety_filter(user_input):
        return "I'm really sorry you're feeling this way. Please reach out to a mental health professional or call an emergency helpline immediately. You are not alone. 💙"

    chain = prompt | llm
    response = chain.invoke({
        "input": user_input,
        "chat_history": chat_history
    })
    return response.content

# ─────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────
st.set_page_config(page_title="Health Query Chatbot", page_icon="🏥")
st.title("🏥 Health Query Chatbot")
st.caption("Ask me any general health questions!")

# Warning Banner
st.warning("⚠️ This chatbot provides general health information only. Always consult a doctor for medical advice.")

# ─────────────────────────────────────────
# Session State
# ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─────────────────────────────────────────
# Chat Input
# ─────────────────────────────────────────
if prompt_input := st.chat_input("Ask a health question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(
                prompt_input,
                st.session_state.chat_history
            )
        st.markdown(response)

    # Update LangChain chat history
    st.session_state.chat_history.append(HumanMessage(content=prompt_input))
    st.session_state.chat_history.append(AIMessage(content=response))

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})