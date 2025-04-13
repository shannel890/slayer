from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Here, you could save to database, send an email, etc.
    print(f"Received message from {name} ({email}): {message}")

    return jsonify({"status": "success", "message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
