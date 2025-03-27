import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os

# Ensure the "audio" folder exists
os.makedirs("audio", exist_ok=True)

st.title("🎙️ Streamlit Audio Recorder")

# User-defined recording duration
duration = st.slider("Select recording duration (seconds)", 1, 10, 5)

if st.button("🎤 Start Recording"):
    samplerate = 44100  # Standard CD-quality sample rate
    st.write("Recording... Speak now!")

    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()  # Wait for recording to finish
    st.success("Recording finished!")

    # Save the audio file
    file_path = "audio/answer.wav"
    wav.write(file_path, samplerate, audio_data)

    st.success(f"Audio saved as `{file_path}`")

    # Play the recorded audio
    st.audio(file_path, format="audio/wav")

    # Provide download option
    with open(file_path, "rb") as audio_file:
        st.download_button("⬇️ Download Recording", audio_file, file_name="answer.wav", mime="audio/wav")
