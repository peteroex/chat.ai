from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def extract_keyword(message):
    words = message.strip().split()
    return words[-1] if words else "product"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    message = data.get("message", "")
    keyword = extract_keyword(message)

    product = {
        "name": f"Best deal for {keyword}",
        "price": "₹1,499",
        "link": f"https://www.amazon.in/s?k={keyword}&tag=your-affiliate-id",
        "image": "https://via.placeholder.com/150"
    }

    return jsonify({
        "response": f'I found a great deal for \"{keyword}\"!',
        "product": product
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or fallback to 5000
    app.run(host='0.0.0.0', port=port)
