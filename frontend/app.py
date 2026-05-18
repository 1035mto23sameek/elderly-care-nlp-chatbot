import requests

import streamlit as st

st.markdown(
    '''
    <style>
    .stTextArea textarea {
        font-size: 20px;
    }

    .stButton button {
        font-size: 20px;
        height: 3em;
        width: 100%;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

#API_URL = "http://localhost:8000/chat"
API_URL = "https://elderly-care-nlp-chatbot-nv9xk3mkgwkrh2kqkhaeqe.streamlit.app/"


st.set_page_config(
    page_title="Elderly Care NLP Chatbot",
    layout="centered"
)


st.title("🧓 Elderly Care NLP Chatbot")

st.write(
    "AI-powered emotional support assistant for elderly wellbeing."
)


# SESSION ID
session_id = st.text_input(
    "Session ID",
    value="elderly_user"
)


# USER INPUT
user_message = st.text_area(
    "How are you feeling today?"
)


if st.button("Send"):

    if user_message:

        response = requests.get(
            API_URL,
            params={
                "message": user_message,
                "session_id": session_id
            }
        )

        data = response.json()

        st.subheader("Chatbot Response")

        st.write(data["bot_response"])

        st.subheader("Detected Emotion")

        st.write(data["predicted_emotion"])

        st.subheader("Detected Intent")

        st.write(data["predicted_intent"])

        st.subheader("Knowledge Support")

        st.write(data["knowledge_support"])

        st.subheader("Conversation Context")

        st.json(data["conversation_context"])