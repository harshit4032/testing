import streamlit as st
import sounddevice as sd
import numpy as np
import wave
import time

st.title("🎙️ Streamlit Voice Recorder")

# Recording parameters
sample_rate = 44100  # Hz
channels = 1
duration = st.slider("Select recording duration (seconds):", 1, 10, 3)

# Function to record audio
def record_audio(duration, sample_rate, channels):
    st.write("Recording... 🎤")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
    sd.wait()
    st.write("Recording finished! ✅")
    return recording

# Button to start recording
if st.button("Start Recording"):
    audio_data = record_audio(duration, sample_rate, channels)

    # Save as a .wav file
    file_name = f"recording_{int(time.time())}.wav"
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

    st.success(f"Recording saved as `{file_name}` 🎧")
    st.audio(file_name, format="audio/wav")

