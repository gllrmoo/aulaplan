from flask import Flask
from src.http.routes_health import health_bp
from src.http.responses import register_error_handlers

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = testing
    app.register_blueprint(health_bp)
    register_error_handlers(app)
    return app