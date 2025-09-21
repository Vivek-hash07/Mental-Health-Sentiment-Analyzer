# utils/voice_input.py

import speech_recognition as sr
import streamlit as st
import tempfile
import os
import io

def transcribe_voice_input():
    """
    Handle voice input using Streamlit's audio recorder widget.
    This works better in web environments than direct microphone access.
    """
    try:
        # Use Streamlit's audio recorder
        audio_file = st.audio_input("🎙️ Click to record your voice:", key="voice_input")
        
        if audio_file is not None:
            st.info("🔍 Processing your speech...")
            
            try:
                # Get the audio bytes from the uploaded file
                audio_bytes = audio_file.read()
                
                # Check if we got valid audio data
                if len(audio_bytes) == 0:
                    st.warning("❌ No audio data received. Please try recording again.")
                    return None
                
                # Save audio to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                    tmp_file.write(audio_bytes)
                    tmp_file_path = tmp_file.name
                    
            except Exception as e:
                st.error(f"❌ Error reading audio file: {e}")
                return None
            
            try:
                # Initialize recognizer
                recognizer = sr.Recognizer()
                
                # Adjust for ambient noise and set timeout
                recognizer.energy_threshold = 300
                recognizer.dynamic_energy_threshold = True
                
                # Debug: Show file info
                file_size = os.path.getsize(tmp_file_path)
                st.info(f"📁 Audio file size: {file_size} bytes")
                
                # Load audio file
                with sr.AudioFile(tmp_file_path) as source:
                    # Adjust for ambient noise
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.record(source)
                    
                # Debug: Show audio info
                st.info(f"🎵 Audio duration: {len(audio.frame_data) / audio.sample_rate:.2f} seconds")
                
                # Try speech recognition
                text = None
                
                try:
                    # Use Google Speech Recognition with optimized settings
                    text = recognizer.recognize_google(
                        audio, 
                        language='en-US',
                        show_all=False
                    )
                    
                    if text and text.strip():
                        st.success(f"✅ Transcription: {text}")
                        return text.strip()
                    else:
                        st.warning("❌ No speech detected in the audio.")
                        return None
                        
                except sr.UnknownValueError:
                    st.warning("❌ Could not understand the audio. Please speak more clearly.")
                    return None
                except sr.RequestError as e:
                    st.error(f"❌ Speech recognition service error: {e}")
                    st.info("💡 This might be due to internet connectivity issues.")
                    return None
                except Exception as e:
                    st.error(f"❌ Unexpected error during speech recognition: {e}")
                    return None
                    
            except Exception as e:
                st.error(f"❌ Error processing audio: {e}")
                return None
            finally:
                # Clean up temporary file
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
        else:
            return None
            
    except Exception as e:
        st.error(f"❌ Error with voice input: {e}")
        return None

def transcribe_voice_input_fallback():
    """
    Fallback method for environments where audio recording doesn't work.
    This provides a text input alternative.
    """
    st.info("🎙️ Voice input is not available in this environment.")
    st.markdown("**Alternative:** Please type your thoughts in the text area below.")
    return None
