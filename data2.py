import streamlit as st
from google import genai
client=genai.Client(api_key="GOOGLE API KEY")
st.title("Ai Product")
prompt=st.chat_input("Describe your product")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
        response=client.models.generate(
        model="gemini-2.5-flash",
        contents=prompt
    )
    with st.chat_message("Assistant"):
        st.write(response.text)