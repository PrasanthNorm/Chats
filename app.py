import streamlit as st
from groq import Groq
from config import settings

# Initialize Groq client
client = Groq(api_key=settings.GROQ_API_KEY)


def get_ai_response(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=settings.MAX_TOKENS,
            temperature=settings.TEMPERATURE
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit UI
st.title("AI Chat Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.markdown(response)

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})