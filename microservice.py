from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

@app.route('/DevOps', methods=['POST'])
def devops():
    api_key = request.headers.get('X-Parse-REST-API-Key')
    
    if api_key != API_KEY:
        return "ERROR", 403

    data = request.json
    message = data.get('message')
    to = data.get('to')
    from_ = data.get('from')

    if message and to and from_:
        return jsonify({"message": f"Hello {to} your message will be sent"})
    return "ERROR", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

