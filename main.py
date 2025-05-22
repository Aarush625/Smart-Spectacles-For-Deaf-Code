from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import json
import time

model_path = r"./model"  # Change this to your actual model path
model = Model(model_path)

samplerate = 16000
q = queue.Queue()
rec = KaldiRecognizer(model, samplerate)

def callback(indata, frames, time_info, status):
    if status:
        print(f"Mic Status: {status}", file=sys.stderr)
    q.put(bytes(indata))

print("\n🎤 Speak — one word per line:\n")

printed_words = set()
last_reset_time = time.time()
reset_interval = 10  # seconds

with sd.RawInputStream(samplerate=samplerate, blocksize=6000, dtype='int16',
                       channels=1, callback=callback, latency='low'):
    try:
        while True:
            # Periodic recognizer reset
            if time.time() - last_reset_time > reset_interval:
                rec.Reset()
                printed_words.clear()
                last_reset_time = time.time()
                print("🔄 Recognizer reset")

            try:
                data = q.get(timeout=1)
            except queue.Empty:
                continue  # No audio data, keep listening

            if rec.AcceptWaveform(data):
                # Final result received, ignoring to keep real-time partials only
                continue

            partial = json.loads(rec.PartialResult())
            text = partial.get("partial", "").strip()
            if not text:
                continue

            for word in text.split():
                if word not in printed_words:
                    print(word)
                    printed_words.add(word)

    except KeyboardInterrupt:
        print("\n🛑 Stopped.")
