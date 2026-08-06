# # 3rd :-  Start the Streamlit server fresh
# streamlit run chatbot_frontend.py

# ============================================================
# chatbot_frontend.py
# This is the UI layer of the chatbot built with Streamlit.
# It calls functions from chatbot_backend.py to get AI responses.
# Run with: streamlit run chatbot_frontend.py
# ============================================================

# streamlit - builds the web UI (buttons, chat boxes, etc.)
import streamlit as st

# Import your backend file as 'demo' so we can call its functions
import chatbot_backend as demo


# -------------------------------------------------------
# STEP 1: Set the page title shown at the top of the browser tab
# and as a heading in the chat UI
# -------------------------------------------------------
st.title("Hi, This is Chatbot Bushraa :sunglasses:")


# -------------------------------------------------------
# STEP 2: Initialize LangChain memory in Streamlit session state
# session_state persists data across Streamlit reruns (each interaction reruns the script)
# We only create memory ONCE - if it already exists, we reuse it
# -------------------------------------------------------
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()  # creates empty [] chat history list


# -------------------------------------------------------
# STEP 3: Initialize the UI chat history in session state
# This is separate from memory - it stores messages for display purposes
# memory = what the AI remembers | chat_history = what the UI shows
# -------------------------------------------------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []  # empty list = no messages shown yet


# -------------------------------------------------------
# STEP 4: Re-render all previous chat messages on screen
# Streamlit reruns the whole script on every interaction,
# so we need to redraw the chat history every time
# -------------------------------------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):   # "user" shows user bubble, "assistant" shows AI bubble
        st.markdown(message["text"])          # display the message text with markdown formatting


# -------------------------------------------------------
# STEP 5: Show the chat input box at the bottom of the screen
# input_text holds whatever the user types and submits
# -------------------------------------------------------
input_text = st.chat_input("Chat with Aamir's Bedrock Bot here")


# -------------------------------------------------------
# STEP 6: Handle the user's message when they hit Enter
# This block only runs when input_text is not empty
# -------------------------------------------------------
if input_text:

    # Show the user's message in the chat UI immediately
    with st.chat_message("user"):
        st.markdown(input_text)

    # Save the user's message to the UI chat history for redisplay on next rerun
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Send the message to the backend and get the AI's response
    # demo_conversation() calls AWS Bedrock and updates memory internally
    chat_response = demo.demo_conversation(
        input_text=input_text,
        memory=st.session_state.memory
    )

    # Show the AI's response in the chat UI
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # Save the AI's response to the UI chat history for redisplay on next rerun
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
