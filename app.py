import os, logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY", "3f351db1-f95a-4df9-b39c-d474a4942c11")

def create_app():
    app = Flask(__name__)

    @app.before_request
    def _check_api_key():
        if request.path in ("/api/health", "/health"):
            return
        key = request.headers.get("X-API-Key", "")
        if key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401

    from routes.users_routes import users_bp
    from routes.documents_routes import documents_bp
    from routes.verifications_routes import verifications_bp
    from routes.kyc_routes import kyc_bp
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(documents_bp, url_prefix="/api/documents")
    app.register_blueprint(verifications_bp, url_prefix="/api/verifications")
    app.register_blueprint(kyc_bp, url_prefix="/api/kyc")

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok"})

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
