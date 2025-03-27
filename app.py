import streamlit as st

st.title("🎙️ Cloud-Compatible Audio Recorder")

# JavaScript to record, play, and download audio
audio_recorder = """
    <script>
    let mediaRecorder;
    let audioChunks = [];
    let audioBlob;

    function startRecording() {
        navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
            mediaRecorder.onstop = () => {
                audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const audioUrl = URL.createObjectURL(audioBlob);

                // Play audio
                const audioPlayer = document.getElementById("audio-player");
                audioPlayer.src = audioUrl;
                audioPlayer.style.display = "block";

                // Download link
                const downloadLink = document.getElementById("download");
                downloadLink.href = audioUrl;
                downloadLink.download = "answer.wav";  // ✅ Save as answer.wav
                downloadLink.style.display = "block";
            };
            mediaRecorder.start();
            document.getElementById("status").innerText = "Recording...";
        });
    }

    function stopRecording() {
        mediaRecorder.stop();
        document.getElementById("status").innerText = "Recording stopped!";
    }
    </script>

    <button onclick="startRecording()">🎤 Start Recording</button>
    <button onclick="stopRecording()">⏹ Stop Recording</button>
    <p id="status"></p>
    <audio id="audio-player" controls style="display: none;"></audio>
    <br>
    <a id="download" style="display: none;">📥 Download answer.wav</a>
"""

# Embed JavaScript into Streamlit
st.components.v1.html(audio_recorder, height=300)
