from flask import Flask, request, jsonify, redirect, render_template
import string
import random

app = Flask(__name__)

# Store URLs in memory (no AWS needed)
url_storage = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_code = generate_short_code()

    url_storage[short_code] = {
        'original_url': original_url,
        'click_count': 0
    }

    short_url = f"http://localhost:5000/{short_code}"

    return jsonify({
        'original_url': original_url,
        'short_url': short_url,
        'short_code': short_code
    })

@app.route('/<short_code>')
def redirect_url(short_code):
    item = url_storage.get(short_code)

    if not item:
        return jsonify({'error': 'URL not found'}), 404

    item['click_count'] += 1
    return redirect(item['original_url'])

@app.route('/stats/<short_code>')
def get_stats(short_code):
    item = url_storage.get(short_code)

    if not item:
        return jsonify({'error': 'Not found'}), 404

    return jsonify({
        'original_url': item['original_url'],
        'short_code': short_code,
        'click_count': item['click_count']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)