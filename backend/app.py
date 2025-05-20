from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

HF_API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # Get token from environment

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    source_lang = data.get("source_lang", "en").lower()
    target_lang = data.get("target_lang", "en").lower()

    if not text:
        return jsonify({"error": "No text to translate"}), 400

    model_url = HF_API_URL.format(src_lang=source_lang, tgt_lang=target_lang)

    payload = {
        "inputs": text
    }

    response = requests.post(model_url, headers=headers, json=payload)

    if response.status_code != 200:
        return jsonify({"error": "Translation API error", "details": response.text}), 500

    try:
        result = response.json()
        # The output is usually a list of dicts with 'translation_text' key
        translation = result[0]["translation_text"]
        return jsonify({"translation": translation})
    except Exception as e:
        return jsonify({"error": f"Parsing translation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
