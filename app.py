import streamlit as st
from emotion_model.analyzer import EmotionAnalyzer
from utils.supportive_message import get_supportive_message
from utils.voice_input import transcribe_voice_input
from utils.pdf_generator import generate_pdf_report
from streamlit_option_menu import option_menu

# Set Streamlit page config
st.set_page_config(
    page_title="Mental Health Sentiment Analyzer",
    page_icon="🧠",
    layout="wide"
)

# Initialize analyzer
analyzer = EmotionAnalyzer()

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="🧭 Navigation",
        options=["Main Analyzer", "Tracker", "About"],
        icons=["activity", "bar-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# ------------------- MAIN ANALYZER PAGE -------------------
if selected == "Main Analyzer":
    st.title("🧠 Mental Health Sentiment Analyzer")
    st.markdown("Analyze your mental state based on your thoughts using state-of-the-art NLP models.")

    text = ""
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
            st.success("✅ Analysis complete!")

            st.markdown("### 📊 Emotion Analysis Result")
            st.write("**Transformer-based Model:**", result['transformer'])
            st.write("**VADER Sentiment:**", result['vader'])
            st.write("**TextBlob Sentiment:**", result['textblob'])

            # Get supportive message
            supportive_message = get_supportive_message(result['transformer'])
            st.markdown("### 💡 Supportive Message")
            st.info(supportive_message)

            # Downloadable PDF Report
            if st.button("📄 Download PDF Report"):
                pdf_path = generate_pdf_report(text, result, supportive_message)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download Report",
                        data=f,
                        file_name=pdf_path.split("/")[-1],
                        mime="application/pdf"
                    )
        else:
            st.warning("Please enter or speak some text to analyze.")

# ------------------- TRACKER PAGE -------------------
elif selected == "Tracker":
    st.switch_page("pages/Tracker.py")

# ------------------- ABOUT PAGE -------------------
elif selected == "About":
    st.title("ℹ️ About this Tool")
    st.markdown("""
This **Mental Health Sentiment Analyzer** is an AI-powered web application that helps users reflect on their mental state through emotional text analysis.

**✨ Features:**
- Voice & Text-based Emotion Analysis
- Sentiment results from Transformer, VADER & TextBlob models
- Personalized supportive messages
- Mood tracking and mood history logs
- PDF report generation of your analysis

Built with ❤️ by [Vivek Sarvaiya]
    """)

# ------------------- SUPPORTIVE MESSAGE FUNCTION (backup) -------------------
# In case you ever remove the separate supportive_message.py file
def get_supportive_message(emotion_label):
    emotion_label = emotion_label.lower()
    messages = {
        "positive": "Keep up the positive mindset! 🌟",
        "negative": "Things might feel tough now, but you're not alone. 💙",
        "neutral": "A balanced mind is powerful. Take a moment to reflect. 🤍"
    }
    return messages.get(emotion_label, "Stay strong, you’ve got this! 💪")
