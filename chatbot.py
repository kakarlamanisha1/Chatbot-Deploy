import streamlit as st
from openai import OpenAI
import os
# import openai

def main():
    st.title("Simple Chatbot")
    #openai.api_key = "REMOVED_SECRET"  # Replace with your OpenAI API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Replace with your OpenAI API key
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=st.session_state.messages
        # )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        # bot_reply = response.choices[0].message["content"]
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

if __name__ == "__main__":
    main()