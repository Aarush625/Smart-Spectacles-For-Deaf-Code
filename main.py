import whisper

# Load the Whisper model - you can try "base", "small", "medium", or "large"
model = whisper.load_model("base")  # or "small", "medium", etc.

# Path to your audio file (WAV, MP3, etc.)
AUDIO_PATH = "audio.wav"  # change this to your file

# Transcribe the audio
result = model.transcribe(AUDIO_PATH)

# Print the output
print("Transcription:", result["text"])
