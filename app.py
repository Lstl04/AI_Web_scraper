from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_website_content_and_clean
from ai import format_content_with_ollama, format_content_with_openai
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/scrape", methods=["POST"])
def scrape():
    try:
        data = request.json
        print("\n✅ Received in Flask:", data)

        url = data.get("url")
        instructions = data.get("instructions")
        model = data.get("model", "ollama")  

        if not url or not instructions:
            return jsonify({"error": "Both URL and instructions are required"}), 400

        cleaned_content = get_website_content_and_clean(url)

        if model == "openai":
            formatted_content = format_content_with_openai(cleaned_content, instructions)
        else:
            formatted_content = format_content_with_ollama(cleaned_content, instructions)

        print("\n✅ Final Response to React:", formatted_content)
        return jsonify({"content": formatted_content})

    except Exception as e:
        print("\n🚨 ERROR OCCURRED:\n", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
