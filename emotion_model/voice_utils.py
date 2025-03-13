# emotion_model/voice_utils.py

import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening for voice input...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"🗣️ Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio")
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        print("⚠️ Google API unavailable or no internet.")
        return "Sorry, the voice recognition service is unavailable."

