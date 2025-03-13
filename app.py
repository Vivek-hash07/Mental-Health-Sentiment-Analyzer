import streamlit as st
from emotion_model.analyzer import EmotionAnalyzer
from utils.supportive_message import get_supportive_message
from utils.selfcare_suggestions import get_selfcare_suggestions
from utils.voice_input import transcribe_voice_input
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(
    page_title="Mental Health Sentiment Analyzer",
    page_icon="🧠",
    layout="wide"
)

# Initialize analyzer
analyzer = EmotionAnalyzer()

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="🧭 Navigation",
        options=["Main Analyzer", "Tracker", "About"],
        icons=["activity", "bar-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Main Analyzer Page
if selected == "Main Analyzer":
    st.title("🧠 Mental Health Sentiment Analyzer")
    st.markdown("Analyze your mental state based on your text input using state-of-the-art NLP models.")

    st.markdown("### 🗣️ Or speak your thoughts:")
    if st.button("🎤 Speak Now"):
        text = transcribe_voice_input()
        if text:
            st.text_area("Recognized Speech:", text, height=100)
        else:
            st.warning("Could not recognize speech. Try again.")
    else:
        text = st.text_area("📝 Enter your thoughts:", placeholder="Type something you're feeling...")

    if st.button("🔍 Analyze"):
        if text.strip():
            with st.spinner("Analyzing..."):
                result = analyzer.analyze_text(text)
            st.success("Analysis complete!")

            st.markdown("### 📊 Emotion Analysis Result")
            st.write("**Transformer-based Model:**", result['transformer'])
            st.write("**VADER Sentiment:**", result['vader'])
            st.write("**TextBlob Sentiment:**", result['textblob'])

            # Supportive message
            supportive_message = get_supportive_message(result['transformer'])
            st.markdown("### 💬 Supportive Message")
            st.info(supportive_message)

            # Self-care suggestions
            suggestions = get_selfcare_suggestions(result['transformer'])
            st.markdown("### 🌿 Self-Care Suggestions")
            for tip in suggestions:
                st.markdown(f"- {tip}")
        else:
            st.warning("Please enter some text to analyze.")

# Tracker Page
elif selected == "Tracker":
    st.switch_page("pages/Tracker.py")

# About Page
elif selected == "About":
    st.title("ℹ️ About this Tool")
    st.markdown("""
    This Mental Health Sentiment Analyzer is an AI-powered tool designed to help users express their thoughts and analyze their emotional well-being.

    **Core Features:**
    - Text-based and voice input
    - Multi-model sentiment analysis (Transformer, VADER, TextBlob)
    - Supportive message generation
    - AI-based self-care suggestions
    - Mood tracker with visualization

    Built with ❤️ by [Vivek Sarvaiya]
    """)
