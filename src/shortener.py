from flask import Blueprint, request, jsonify, current_app, redirect
import uuid
import json

shortener = Blueprint("shortener", __name__)
index_bp = Blueprint("index", __name__)
red = Blueprint("red", __name__)

@shortener.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    urls = current_app.redis_client.get("urls")
    if urls:
        urls = json.loads(urls)
        if url in urls:
            return jsonify({"error": "URL already shortened"}), 400
    else:
        urls = []

    short_id = str(uuid.uuid4())[:6]
    current_app.redis_client.set(short_id, url)
    urls.append(url)
    current_app.redis_client.set("urls", json.dumps(urls))
    return jsonify({"short_id": short_id}), 201

@index_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, World!"})

@red.route("/red/<short_id>", methods=["GET"])
def redirect_to_url(short_id):
    url = current_app.redis_client.get(short_id)
    if not url:
        return jsonify({"error": "URL not found"}), 404
    url = url.decode("utf-8")
    if not url.startswith("https://"):
        url = "https://" + url
    return redirect(url, code=302)