from flask import Flask
api = Flask(__name__)
@api.get("/api/health")
def health():
    return "ok",200

if __name__ == "__main__":
    api.run(host="0.0.0.0",port=5000)

