# emotion_model/analyzer.py

from emotion_model.model_utils import load_transformer_model, analyze_with_vader, analyze_with_textblob

class EmotionAnalyzer:
    def __init__(self):
        self.transformer_pipeline, _ = load_transformer_model()

    def analyze_text(self, text):
        return {
            "transformer": self._analyze_with_transformer(text),
            "vader": analyze_with_vader(text),
            "textblob": analyze_with_textblob(text)
        }

    def _analyze_with_transformer(self, text):
        result = self.transformer_pipeline(text)[0]  # Using the pipeline directly
        return result['label']

# Example usage
if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    test_text = "I feel really anxious and overwhelmed today."
    print("\nText:", test_text)
    print("Analysis:", analyzer.analyze_text(test_text))
