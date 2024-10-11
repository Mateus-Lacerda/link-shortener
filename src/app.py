from flask import Flask, jsonify
import traceback
from werkzeug.exceptions import HTTPException
import redis
import os

from src.shortener import shortener, red

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/10")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(shortener)
    app.register_blueprint(red)

    redis_client = redis.from_url(REDIS_URL)
    app.redis_client = redis_client

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        error=str(e)
        traceback_=str(traceback.format_exc())
        print(f"Error: {error}")
        print(f"Traceback: {traceback_}")
        return jsonify(error, traceback_), code

    app.errorhandler(HTTPException)(handle_error)
    app.errorhandler(Exception)(handle_error)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)