from flask import Flask, request
from reranker.rerank_service import rerank_results

app = Flask(__name__)


@app.route("/apis/hello", methods=["GET", "POST"])
def hello_world():
    return {"message": "hello"}


@app.route("/apis/rerank", methods=["POST"])
def rerank_api():
    data = request.get_json()
    results = rerank_results(data["query"], data["hits"])
    return results[0].to_dict()
