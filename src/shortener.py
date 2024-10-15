from flask import Blueprint, request, jsonify, current_app, redirect, url_for
import uuid

shortener = Blueprint("shortener", __name__)
red = Blueprint("red", __name__)

@shortener.route("/", methods=["POST"])
def shorten():
    
    data = request.get_json()
    url = str(data.get("url"))

    if not url:
        return jsonify({"error": "URL is required"}), 400

    chave = current_app.redis_client.get(f"urls:destinos:{url}")

    if chave:
        return url_for("red.redirect_to_url", short_id=chave.decode("utf-8"), _external=True), 200

    short_id = str(uuid.uuid4())[:6]
    current_app.redis_client.set(f"urls:chaves:{short_id}", url)
    current_app.redis_client.set(f"urls:destinos:{url}", short_id)

    return url_for("red.redirect_to_url", short_id=short_id, _external=True), 201


@red.route("/", methods=["GET"])
def redirect_to_url(short_id):
    url = current_app.redis_client.get(f"urls:chaves:{short_id}")
    if not url:
        return jsonify({"error": "URL not found"}), 404
    url = url.decode("utf-8")
    return redirect(url, code=302)