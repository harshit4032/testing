import streamlit as st
import pyaudio
import wave

# Audio Recording Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "recorded_audio.wav"

def record_audio():
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    st.write("🎤 **Recording... Speak Now!**")
    
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    st.write("✅ **Recording Finished!**")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save audio file
    with wave.open(OUTPUT_FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    return OUTPUT_FILENAME

st.title("🎙️ Streamlit Audio Recorder")

if st.button("Start Recording"):
    audio_file = record_audio()
    st.audio(audio_file, format="audio/wav", start_time=0)

    with open(audio_file, "rb") as f:
        st.download_button(label="📥 Download Recording", data=f, file_name="recorded_audio.wav")
