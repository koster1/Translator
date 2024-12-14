from flask import Flask, render_template, request
from transformers import pipeline
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Load the translation model
MODEL_NAME = os.getenv("MODEL_NAME", "Helsinki-NLP/opus-mt-en-fi")
translator = pipeline("translation", model=MODEL_NAME)

MAX_LENGTH = 2000  # Maximum number of characters in the users input

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        translated_text = translate_text(text)
    return render_template("index.html", translated_text=translated_text)

def translate_text(text: str) -> str:
    normalized_text = text.strip().capitalize()  # Clean text
    
    # Split text into chunks if it's too long
    if len(normalized_text) > MAX_LENGTH:
        chunks = split_text_into_chunks(normalized_text, MAX_LENGTH)
        translated_chunks = [translator(chunk)[0]['translation_text'] for chunk in chunks]
        return " ".join(translated_chunks)
    
    # Skip translating numbers or symbols alone
    if re.match(r'^[\d\s\W]+$', normalized_text):
        return normalized_text
    
    try:
        result = translator(normalized_text)
        return result[0]['translation_text']
    except Exception as e:
        return f"Error: Unable to translate text. Details: {str(e)}"

def split_text_into_chunks(text: str, max_length: int):
    chunks = []
    current_chunk = ""
    
    # Split text by sentence
    for sentence in text.split('.'):
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

if __name__ == "__main__":
    app.run(debug=True)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    return "An unexpected error occurred. Please try again later.", 500
