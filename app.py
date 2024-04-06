import streamlit as st
import pyttsx3

def text_to_speech(text, rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("Text-to-Speech")
    
    st.write("Enter the text ")
    text_input = st.text_area("Input Text")

    rate = st.slider("Select Speech Rate", min_value=100, max_value=300, step=10, value=200)

    if st.button("Convert to Speech"):
        if text_input:
            text_to_speech(text_input, rate)
            st.success("Speech generated successfully!")
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()
