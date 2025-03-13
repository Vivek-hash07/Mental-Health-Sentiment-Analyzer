# utils/voice_input.py

import speech_recognition as sr

def transcribe_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Listening... Please speak clearly.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"✅ Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand the audio.")
        return "Voice not clear"
    except sr.RequestError as e:
        print(f"❌ Error with Google Speech Recognition: {e}")
        return "Speech recognition service error"
