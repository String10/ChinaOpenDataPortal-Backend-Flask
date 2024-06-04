from flask import Flask

app = Flask(__name__)


@app.route("/apis/hello", methods=["GET", "POST"])
def hello_world():
    return {"message": "hello"}
