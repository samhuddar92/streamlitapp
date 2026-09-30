import streamlit as st
from langchain_groq import ChatGroq

GROQ_API_KEY = "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"

# streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI Chatbot")
api_key_configured = GROQ_API_KEY != "YOUR_GROQ_API_KEY"
if not api_key_configured:
    st.warning("Set GROQ_API_KEY in chatbot.py to enable chat.")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input box
user_prompt = st.chat_input("Ask Chatbot...", disabled=not api_key_configured)

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.0,
        api_key=GROQ_API_KEY,
    ).invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
