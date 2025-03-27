import streamlit as st
import speech_recognition as sr
import wave

st.title("🎙️ Streamlit Audio Recorder")

# Function to record audio
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Speak now...")
        audio_data = recognizer.listen(source)
        st.write("✅ Recording finished!")

        # Save audio to a file
        filename = "recorded_audio.wav"
        with open(filename, "wb") as f:
            f.write(audio_data.get_wav_data())

        return filename

# Record when button is clicked
if st.button("Start Recording"):
    audio_file = record_audio()
    st.audio(audio_file, format="audio/wav")

    # Provide download option
    with open(audio_file, "rb") as f:
        st.download_button(label="📥 Download Recording", data=f, file_name="recorded_audio.wav")
