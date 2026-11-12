from flask import Flask, jsonify, request

app = Flask(__name__)

messages = []

@app.route("/health")

def health():
    return jsonify({"status":"ok"})
@app.route("/messages",methods=["GET"])
def get_message():
    return jsonify(messages)

@app.route("/messages",methods=["POST"])
def add_message():
    data = request.get_json()
    messages.append(data)
    return jsonify({"success":True,"message":data})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
