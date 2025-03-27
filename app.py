import streamlit as st
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

st.title("🎙️ Streamlit Audio Recorder")

# Define audio settings
SAMPLE_RATE = 44100  # CD-quality audio
DURATION = 5  # Record for 5 seconds

def record_audio():
    st.write("🎤 Recording...")
    audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    st.write("✅ Recording complete!")

    # Save the recorded audio
    filename = "recorded_audio.wav"
    write(filename, SAMPLE_RATE, audio_data)
    return filename

# Start recording when button is clicked
if st.button("Start Recording"):
    audio_file = record_audio()
    st.audio(audio_file, format="audio/wav")

    # Provide a download option
    with open(audio_file, "rb") as f:
        st.download_button(label="📥 Download Recording", data=f, file_name="recorded_audio.wav")
