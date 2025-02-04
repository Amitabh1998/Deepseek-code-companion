import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS styling
st.markdown("""
<style>
    /* Existing styles */
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    
    /* Add these new styles for select box */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    
    .stSelectbox svg {
        fill: white !important;
    }
    
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    
    /* For dropdown menu items */
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
st.title("  💻 AI Code Companion")
st.caption("  🚀 Your ultimate AI coding Assistant")

# Sidebar configuration
with st.sidebar:
    st.header("Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "codellama:13b"], index = 0
    )

    st.divider()
    st.markdown('### Model Capabilities')
    st.markdown("""
    - Python Expert
    - Debugging Assistant
    - Code Documentation
    - Solution Design
    """)

    st.divider()
    st.markdown("Build with [Ollama](https://ollama.ai/)  | [Langchain](https://python.langchain.com/)")

# initiate the chat engine

llm_engine = ChatOllama(model= selected_model, base_url="http://localhost:11434", temperature = 0.3)

system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English. "
)

# Session State Management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role":"ai", "content":"Hi! I'm your AI code companion. How can I help you with your coding pursuits?"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your question here...")

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            content = msg["content"].replace("{", "{{").replace("}", "}}")
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            content = msg["content"].replace("{", "{{").replace("}", "}}")
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role":"user", "content": user_query})

    # Generate AI response
    with st.spinner("Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)

    # Add AI response to log
    st.session_state.message_log.append({"role":"ai", "content": ai_response})

    # Rerun to update chat display
    st.rerun()




