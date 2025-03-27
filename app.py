import streamlit as st
import pydub
import speech_recognition as sr
import numpy as np
import os
from pydub import AudioSegment
from pydub.playback import play

# Ensure the "audio" folder exists
os.makedirs("audio", exist_ok=True)

st.title("🎙️ Streamlit Audio Recorder (Using pydub)")

duration = st.slider("Select recording duration (seconds)", 1, 10, 5)

if st.button("🎤 Start Recording"):
    st.write("Recording... Speak now!")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.record(source, duration=duration)

    st.success("Recording finished!")

    # Convert SpeechRecognition audio to WAV
    file_path = "audio/answer.wav"
    with open(file_path, "wb") as f:
        f.write(audio_data.get_wav_data())

    st.success(f"Audio saved as `{file_path}`")

    # Play the recorded audio
    st.audio(file_path, format="audio/wav")

    # Provide download option
    with open(file_path, "rb") as audio_file:
        st.download_button("⬇️ Download Recording", audio_file, file_name="answer.wav", mime="audio/wav")
