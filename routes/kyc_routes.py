import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
kyc_bp = Blueprint("kyc", __name__)

@kyc_bp.route("/kyc/stats", methods=["GET"])
def kyc_stats_get():
    """Obtenir les statistiques globales des vérifications KYC"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"kyc_stats_get error: {e}")
        return jsonify({"error": str(e)}), 500

@kyc_bp.route("/kyc/webhook", methods=["POST"])
def kyc_webhook_post():
    """Endpoint webhook pour recevoir les résultats de vérification externe"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"kyc_webhook_post error: {e}")
        return jsonify({"error": str(e)}), 500

