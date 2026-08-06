## 3rd :- streamlit run chatbot_frontend2.py

# ============================================================
# chatbot_frontend2.py
# A more polished Streamlit frontend for the Bedrock chatbot.
# This file is separate from the original frontend and does not
# modify any existing files.
# Run with: streamlit run chatbot_frontend2.py
# ============================================================

import streamlit as st
import chatbot_backend as demo


st.set_page_config(
    page_title="NovaMind AI",
    page_icon="🤖",
    layout="wide",
)


# -----------------------------
# Custom styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 45%, #f1f5f9 100%);
        color: #0f172a;
    }
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }
    .hero-box {
        padding: 1.2rem 1.4rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
    }
    .sidebar .block-container {
        background: #ffffff;
        color: #0f172a;
    }
    div[data-testid="stChatMessage"] {
        padding: 0.4rem 0;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stButton > button {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Session state initialization
# -----------------------------
if "memory" not in st.session_state:
    st.session_state.memory = demo.demo_memory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "bot_name" not in st.session_state:
    st.session_state.bot_name = "NovaMind"

if "response_style" not in st.session_state:
    st.session_state.response_style = "Balanced"


# -----------------------------
# Sidebar controls
# -----------------------------
with st.sidebar:
    st.markdown("## ⚙️ Control Center")
    st.markdown("Choose your assistant personality and manage the conversation.")

    bot_options = ["NovaMind", "CloudPilot", "Bedrock Pro", "ByteBot", "Aamir's chatbot"]
    selected_name = st.selectbox(
        "Choose chatbot name",
        bot_options,
        index=bot_options.index(st.session_state.bot_name) if st.session_state.bot_name in bot_options else 0,
    )
    st.session_state.bot_name = selected_name

    style_options = ["Balanced", "Concise", "Detailed", "Creative"]
    response_style = st.selectbox(
        "Response style",
        style_options,
        index=style_options.index(st.session_state.response_style) if st.session_state.response_style in style_options else 0,
    )
    st.session_state.response_style = response_style

    if st.button("🧹 Clear Conversation", use_container_width=True):
        st.session_state.memory = demo.demo_memory()
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    st.markdown("### Quick Info")
    st.caption("This version uses the same backend logic as the original chatbot, but adds a more polished Streamlit experience.")


# -----------------------------
# Header hero section
# -----------------------------
st.markdown(
    f"""
    <div class="hero-box">
        <h1 style="margin-bottom:0.2rem;">{st.session_state.bot_name} AI</h1>
        <p style="margin:0; color:#cbd5e1;">Your smart assistant for AWS, cloud concepts, and practical guidance.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Helper for style-aware prompts
# -----------------------------

def build_prompt(user_input: str, style: str) -> str:
    style_map = {
        "Balanced": "Answer clearly and helpfully. Be friendly and practical.",
        "Concise": "Answer briefly and directly. Keep it short and useful.",
        "Detailed": "Answer in a detailed, structured, and informative way with examples when helpful.",
        "Creative": "Answer with a vivid, engaging, and creative tone while staying useful.",
    }
    instruction = style_map.get(style, style_map["Balanced"])
    return f"{instruction}\n\nUser question: {user_input}"


# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "🤖"):
        st.markdown(message["text"])


# -----------------------------
# Chat input
# -----------------------------
input_text = st.chat_input(f"Ask {st.session_state.bot_name} anything...")

if input_text:
    with st.chat_message("user", avatar="🧑"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role": "user", "text": input_text})

    prompt_with_style = build_prompt(input_text, st.session_state.response_style)

    with st.spinner("Thinking..."):
        chat_response = demo.demo_conversation(
            input_text=prompt_with_style,
            memory=st.session_state.memory,
        )

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
