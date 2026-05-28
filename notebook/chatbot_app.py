
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

# Page configuration
st.set_page_config(
    page_title="Chatbot con LLM",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chatbot con LLM")

# Sidebar for API key
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("GROQ API Key", type="password")

    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    if st.button("Limpiar historial"):
        st.session_state.messages = []
        st.rerun()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Escribe tu mensaje..."):
    if not api_key:
        st.error("Por favor, introduce tu API key en la barra lateral.")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    llm = ChatGroq(
                        model_name="llama-3.3-70b-versatile",
                        temperature=0.7
                    )

                    # Build messages
                    messages = [SystemMessage(content="Eres un asistente amable.")]

                    for msg in st.session_state.messages:
                        if msg["role"] == "user":
                            messages.append(HumanMessage(content=msg["content"]))
                        else:
                            messages.append(AIMessage(content=msg["content"]))

                    response = llm.invoke(messages)
                    st.write(response.content)

                    # Add assistant response to history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response.content
                    })

                except Exception as e:
                    st.error(f"Error: {e}")
