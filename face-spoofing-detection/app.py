from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detection', methods=['POST'])
def detection():
    # Here you would handle the face spoofing detection logic
    # For now, we will just return a placeholder response
    data = request.json
    # Process the data and perform detection
    result = {
        'success': True,
        'message': 'Face spoofing detection completed.',
        'data': data  # Placeholder for actual detection results
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)