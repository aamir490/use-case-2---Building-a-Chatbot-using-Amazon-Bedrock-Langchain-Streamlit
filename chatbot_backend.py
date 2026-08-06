# 1st :- run this
# python -c "import chatbot_backend as b; mem = b.demo_memory(); print(b.demo_conversation('Hello, what is AWS Bedrock?', mem))"

# ============================================================
# chatbot_backend.py
# This file handles all the AI logic for the chatbot.
# The frontend (chatbot_frontend.py) calls functions from here.
# ============================================================

# ChatBedrockConverse - connects Python to AWS Bedrock AI models
from langchain_aws import ChatBedrockConverse

# HumanMessage - wraps user messages
# AIMessage    - wraps AI/assistant responses
# SystemMessage - sets the AI's behavior/personality
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ChatPromptTemplate   - builds the full prompt structure
# MessagesPlaceholder  - inserts the chat history into the prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# -------------------------------------------------------
# FUNCTION 1: demo_chatbot()
# Creates and returns the AI model connection to AWS Bedrock
# -------------------------------------------------------
def demo_chatbot():
    demo_llm = ChatBedrockConverse(
        credentials_profile_name='default',  # uses your AWS 'default' profile credentials
        model="amazon.nova-pro-v1:0",        # the Bedrock model to use
        temperature=0.1,                     # lower = more focused answers (0.0 to 1.0)
        max_tokens=1000                      # maximum length of the AI response
    )
    return demo_llm  # returns the model object (not a response yet)


# -------------------------------------------------------
# FUNCTION 2: demo_memory()
# Creates and returns an empty chat history list
# Each conversation turn gets stored here as messages
# This replaces the old ConversationSummaryBufferMemory
# -------------------------------------------------------
def demo_memory():
    return []  # empty list = fresh conversation with no history


# -------------------------------------------------------
# FUNCTION 3: demo_conversation()
# The main function that sends a message to the AI and gets a reply
# Parameters:
#   input_text - the user's typed message
#   memory     - the list of previous messages (chat history)
# -------------------------------------------------------
def demo_conversation(input_text, memory):

    # Step 1: Get the AI model connection
    llm = demo_chatbot()

    # Step 2: Build the prompt structure
    # - SystemMessage sets how the AI should behave
    # - MessagesPlaceholder inserts the full chat history
    # - ("human", "{input}") adds the current user message at the end
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),  # previous messages go here
        ("human", "{input}")                           # current user message goes here
    ])

    # Step 3: Chain the prompt and the model together
    # The | operator means: feed prompt output into the model
    chain = prompt | llm

    # Step 4: Send everything to the AI and get a response
    response = chain.invoke({
        "history": memory,      # pass the chat history
        "input": input_text     # pass the current user message
    })

    # Step 5: Save this turn to memory so the AI remembers it next time
    memory.append(HumanMessage(content=input_text))       # save user message
    memory.append(AIMessage(content=response.content))    # save AI reply

    # Step 6: Return just the text of the AI reply back to the frontend
    return response.content


# Links:
# https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html
# https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AmazonTitanText_section.html


# # Run a one-line Python command from the terminal
# python -c "

# # Import the chatbot_backend module and give it a shorter alias 'b'
# import chatbot_backend as b;

# # Create a demo conversation memory object.
# # This simulates the chatbot's memory so it can remember previous messages.
# mem = b.demo_memory();

# # Start a demo conversation.
# # User Prompt: 'Hello, what is AWS Bedrock?'
# # The chatbot uses the memory object (mem) to generate a response.
# # print() displays the chatbot's response in the terminal.
# print(b.demo_conversation('Hello, what is AWS Bedrock?', mem))"


# python -c "import chatbot_backend as b; mem = b.demo_memory(); print(b.demo_conversation('Hello, what is AWS Bedrock?', mem))"
