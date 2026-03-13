import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
documents_bp = Blueprint("documents", __name__)

@documents_bp.route("/users/<user_id>/documents", methods=["POST"])
def users_user_id_documents_post(user_id):
    """Uploader une piece d identite pour un utilisateur"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_post error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents", methods=["GET"])
def users_user_id_documents_get(user_id):
    """Lister tous les documents d un utilisateur"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_get error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>", methods=["GET"])
def users_user_id_documents_document_id_get(user_id, document_id):
    """Recuperer les details d un document specifique"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_get error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>", methods=["DELETE"])
def users_user_id_documents_document_id_delete(user_id, document_id):
    """Supprimer un document uploade"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_delete error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>/status", methods=["PATCH"])
def users_user_id_documents_document_id_status_patch(user_id, document_id):
    """Mettre a jour le statut de validation d un document"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_status_patch error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/selfie", methods=["POST"])
def users_user_id_selfie_post(user_id):
    """Uploader le selfie de l utilisateur pour verification"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"users_user_id_selfie_post error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/documents/types", methods=["GET"])
def documents_types_get():
    """Lister les types de documents acceptes"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"documents_types_get error: {e}")
        return jsonify({"error": str(e)}), 500
