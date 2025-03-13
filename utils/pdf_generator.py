from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_pdf_report(text, results, supportive_message, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_dir, f"mental_health_report_{timestamp}.pdf")

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "🧠 Mental Health Sentiment Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.drawString(50, height - 130, "📝 Your Input:")
    text_lines = text.split('\n')
    y = height - 150
    for line in text_lines:
        c.drawString(60, y, f"- {line}")
        y -= 20

    y -= 10
    c.drawString(50, y, "📊 Emotion Analysis Results:")
    y -= 20
    for key, val in results.items():
        c.drawString(60, y, f"{key.capitalize()}: {val}")
        y -= 20

    y -= 10
    c.drawString(50, y, "💡 Supportive Message:")
    y -= 20
    c.drawString(60, y, supportive_message)

    c.save()
    return filename
