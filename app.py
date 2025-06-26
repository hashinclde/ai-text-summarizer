import streamlit as st

def summarize_text(text):
    sentences = text.split('. ')
    summary = '. '.join(sentences[:2]) + '...'
    return summary

st.title("🧠 AI Text Summarizer")
st.write("Paste a paragraph or article below and click to get a short summary!")

text = st.text_area("✍️ Enter text to summarize", height=300)

if st.button("✨ Summarize"):
    if text:
        result = summarize_text(text)
        st.success("Here's your summary:")
        st.write(result)
    else:
        st.warning("Please enter some text above.")
