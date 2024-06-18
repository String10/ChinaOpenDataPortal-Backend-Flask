from flask import Flask, request
from flask_caching import Cache
from hashlib import sha256

from reranker.rerank_service import rerank_results
from explain.explain_service import explain_result
from utils.config import CACHE_DIR, CACHE_TIMEOUT

app = Flask(__name__)
cache = Cache(
    app,
    config={
        "CACHE_TYPE": "FileSystemCache",
        "CACHE_DIR": CACHE_DIR,
        "CACHE_DEFAULT_TIMEOUT": CACHE_TIMEOUT,
    },
)


@app.route("/apis/hello", methods=["GET", "POST"])
def hello_world():
    return {"message": "hello"}


@app.route("/apis/rerank", methods=["POST"])
def rerank_api():
    data = request.get_json()
    results = rerank_results(data["query"], data["hits"])
    return results[0].to_dict()


@app.route("/apis/explain", methods=["POST"])
def explain_api():
    data = request.get_json()

    cache_key = (
        "explain-%s"
        % sha256(f'{data["query"]}-{data["metadata"]}'.encode()).hexdigest()
    )
    explanation = cache.get(cache_key)
    if explanation is not None:
        return explanation

    explanation = explain_result(data["query"], data["metadata"])
    if explanation != "NONE":
        cache.set(cache_key, explanation)
    return explanation
