# utils/selfcare_suggestions.py

def get_selfcare_suggestions(emotion_label):
    emotion_label = emotion_label.lower()
    suggestions = {
        "positive": [
            "✨ Keep a gratitude journal.",
            "🎶 Celebrate with your favorite music.",
            "🧘 Share your good energy with someone else today!"
        ],
        "negative": [
            "📝 Try writing down your feelings in a journal.",
            "🧘‍♀️ Practice 5 minutes of deep breathing.",
            "📱 Reach out to a trusted friend or loved one.",
            "🚶‍♂️ Go for a peaceful walk in nature."
        ],
        "neutral": [
            "☕ Take a short mindful tea/coffee break.",
            "📖 Read a book or listen to calming music.",
            "💧 Hydrate and stretch your body for a few minutes."
        ]
    }
    return suggestions.get(emotion_label, ["💪 Stay strong and take care of yourself today."])
