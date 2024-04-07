import streamlit as st
import tempfile
import os
import nltk
from gtts import gTTS

# Download necessary NLTK resources
nltk.download('punkt')

def text_to_speech(text, language='en'):
    """Converts text to speech and plays it in the web page."""
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Create a temporary directory for audio files
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_files = []

        # Convert each sentence to speech and save to temporary files
        for idx, sentence in enumerate(sentences):
            tts = gTTS(text=sentence, lang=language, slow=False)
            filename = f"output_{idx}.mp3"
            filepath = os.path.join(tmpdir, filename)
            tts.save(filepath)
            audio_files.append(filepath)

        # Play the audio files
        for file in audio_files:
            st.audio(file, format='audio/mp3')

        # Clean up temporary audio files (not strictly necessary in this case)
        for file in audio_files:
            os.remove(file)

    st.success("Text-to-speech conversion complete.")

# Create a Streamlit app interface
def home():
    st.write("""
    <style>
    body {
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)


   

    input_text = st.text_area("Enter text to convert to speech")

    if st.button("Convert to Speech"):
        if input_text:
            text_to_speech(input_text)
        else:
            st.warning("Please enter some text to convert.")
def about():
    st.write("<h1 style='text-align: center; color: white;'>About</h1>", unsafe_allow_html=True)
    st.write("""
    <div style='color: Black; text-align: center;'>
        <p>When working with Text-to-Speech (TTS) using NLTK (Natural Language Toolkit) and gTTS (Google Text-to-Speech), the data modeling involves basic linguistic processing with NLTK to handle text input and generate phonetic representations (if needed), followed by using gTTS to synthesize speech.</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(layout="wide")
    st.title("Text To Speech App")

    
    # Apply background image to the entire application
    st.write("""
    <style>
    body {
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F09%2Flisten-to-our-major-text-to-speech-upgrades-for-64-bit-devices.html&psig=AOvVaw25Oz59Ev7259wySTG7AE77&ust=1712596542470000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKift8bNsIUDFQAAAAAdAAAAABAE');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)
    # Create the tab layout
    page = st.sidebar.radio("Select a page", ["Home", "About"])

    # Show the appropriate page based on the user selection
    if page == "Home":
        home()
    elif page == "About":
        about()

main()
