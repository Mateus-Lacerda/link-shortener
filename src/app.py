from flask import Flask
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

    return app

if __name__ == "__main__":
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=FLASK_ENV == "development")