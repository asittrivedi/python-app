from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_input():
    data = request.json
    if not data or 'input' not in data:
        return jsonify({'error': 'No input provided'}), 400
    return jsonify({'message': f"Received input: {data['input']}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
