import streamlit as st
from utils import call_llama


st.title("🚀 Streamlit Chatbot💬 powered by LLAMA:llama:")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner('Generating response...	:hourglass_flowing_sand:'):
            msg = call_llama('llama2', prompt)['response']
        #msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)