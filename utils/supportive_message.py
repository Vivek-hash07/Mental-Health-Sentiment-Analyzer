# utils/supportive_message.py

def get_supportive_message(emotion):
    supportive_messages = {
        "POSITIVE": "Keep shining! It's wonderful to hear you're feeling positive. 😊",
        "NEGATIVE": "It's okay to feel this way. Take a deep breath and remember you're not alone. 💙",
        "NEUTRAL": "Staying balanced is a strength. Keep going with steady steps. ⚖️",
        "Positive": "Glad to know you're doing well! 🌟",
        "Negative": "Things might be tough right now, but you’re tougher. 💪",
        "Neutral": "Every feeling matters — you're doing fine. ✨",
        "Happy": "Happiness is contagious — keep spreading the joy!",
        "Sad": "Your feelings are valid. It’s okay to not be okay sometimes. 💗",
        "Angry": "Take a moment to breathe. You have the strength to move through this. 🔥",
        "Anxious": "You’re doing your best, and that’s more than enough. 🧘",
        "Excited": "That energy is amazing! Embrace it fully. 🎉",
        "Tired": "Rest is productive. Make time to recharge. 😴"
    }

    return supportive_messages.get(emotion, "You're strong. No matter what you're feeling, you matter. 💜")
