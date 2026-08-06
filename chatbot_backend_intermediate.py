
# 2nd :- To test it:
## python chatbot_backend_intermediate.py


# ============================================================
# chatbot_backend_intermediate.py
# This is a practice/test file from the Udemy course.
# It tests a direct raw connection to AWS Bedrock using DeepSeek model.
# NOT connected to the frontend - used for learning purposes only.
# ============================================================

# ChatBedrockConverse - connects Python to AWS Bedrock AI models
from langchain_aws import ChatBedrockConverse

# HumanMessage - wraps user messages for the model
from langchain_core.messages import HumanMessage


# -------------------------------------------------------
# FUNCTION: demo_chatbot()
# Sends a message directly to the DeepSeek model on Bedrock
# and returns the raw response
# Parameter:
#   input_text - the question/message to send to the model
# -------------------------------------------------------
def demo_chatbot(input_text):
    # Create the Bedrock model connection
    demo_llm = ChatBedrockConverse(
        credentials_profile_name='default',   # uses your AWS 'default' profile
        model="us.deepseek.r1-v1:0",          # DeepSeek model (different from main chatbot)
        temperature=0.1,                      # lower = more focused answers
        max_tokens=1000                       # max length of response
    )

    # Wrap the input as a HumanMessage and send it to the model
    response = demo_llm.invoke([HumanMessage(content=input_text)])

    # Return just the text content of the response
    return response.content


# -------------------------------------------------------
# Test block - only runs when this file is executed directly
# Will NOT run if this file is imported by another file
# -------------------------------------------------------
if __name__ == "__main__":
    # Test question to verify the connection works
    test_question =  "What is AWS s3?"    # "What is AWS Bedrock?" 

    print(f"Sending test question: {test_question}\n")
    response = demo_chatbot(test_question)
    print("Response from DeepSeek model:")
    print(response)


# Links:
# https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html
# https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AmazonTitanText_section.html
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html
