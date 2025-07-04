from flask import Flask, jsonify, request
import base64
import json

app = Flask(__name__)


#Hier bitte nicht nach der geheimen Nachricht suchen! Bitte gehen Sie weiter! 
base64_str = "eyJlYXN0ZXJfZWdnIjogIkNvbmdyYXR1bGF0aW9ucyEgWW91IGZvdW5kIHRoZSBzZWNyZXQgRWFzdGVyIEVnZyEifQ=="

# Öffentliche Beispiel-Daten
data = {
    "message": "Hello, World!",
    "content": ["item1", "item2", "item3"],
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ],
    "settings": {
        "theme": "light",
        "notifications": True,
        "language": "en"
    },
    "status": "active"
}

@app.route('/')
def home():
    return "Welcome to the Flask API! Use the available endpoints to interact with the data."

@app.route('/api/message')
def get_message():
    return jsonify({"message": data["message"]})

@app.route('/api/content')
def get_content():
    return jsonify({"content": data["content"]})

@app.route('/api/users')
def get_users():
    return jsonify({"users": data["users"]})

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = next((user for user in data["users"] if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/settings', methods=['GET', 'POST'])
def manage_settings():
    if request.method == 'POST':
        new_settings = request.json
        data["settings"].update(new_settings)
        return jsonify({"message": "Settings updated successfully", "settings": data["settings"]})
    else:
        return jsonify({"settings": data["settings"]})

@app.route('/api/easteregg')
def easter_egg():
    # Dekodieren Sie die Base64-Nachricht
    base64_bytes = base64_str.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message_str = message_bytes.decode('utf-8')

    # Konvertieren Sie die Nachricht zurück in ein Dictionary
    secret_message = json.loads(message_str)

    return jsonify(secret_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
