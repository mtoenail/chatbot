from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://yourwordpress.com"])  # Replace with your WP domain

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    reply = f"You said: {user_message}"  # Replace with your chatbot logic
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
