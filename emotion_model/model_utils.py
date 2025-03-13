# emotion_model/model_utils.py

from transformers import pipeline
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_transformer_model():
    """
    Loads a HuggingFace sentiment analysis pipeline.
    Returns:
        tuple: (pipeline, tokenizer) - tokenizer is set to None for consistency.
    """
    transformer_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return transformer_pipeline, None  # tokenizer not used explicitly here

def analyze_with_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

def analyze_with_vader(text):
    vader_analyzer = SentimentIntensityAnalyzer()
    score = vader_analyzer.polarity_scores(text)["compound"]
    return "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"
