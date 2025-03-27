import streamlit as st
import os
import time
from pydub import AudioSegment
from pydub.playback import play

st.title("🎙️ Cloud-Compatible Audio Recorder")

DURATION = 5  # Duration in seconds
OUTPUT_FILE = "recorded_audio.wav"

# Function to record audio using ffmpeg
def record_audio():
    st.write("🎤 Recording...")
    
    os.system(f"ffmpeg -f alsa -t {DURATION} -i default {OUTPUT_FILE}")  # Uses ALSA (Linux default)
    
    st.write("✅ Recording complete!")
    return OUTPUT_FILE

# Button to start recording
if st.button("Start Recording"):
    audio_file = record_audio()
    st.audio(audio_file, format="audio/wav")

    # Provide a download option
    with open(audio_file, "rb") as f:
        st.download_button(label="📥 Download Recording", data=f, file_name="recorded_audio.wav")
