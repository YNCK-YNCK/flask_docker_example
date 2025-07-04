from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel-Daten
data = {
    "message": "Hello, World!",
    "content": ["item1", "item2", "item3"]
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
