import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
documents_bp = Blueprint("documents", __name__)

@documents_bp.route("/users/<user_id>/documents", methods=["POST"])
def users_user_id_documents_post():
    """Uploader une pièce d'identité pour un utilisateur"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_post error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents", methods=["GET"])
def users_user_id_documents_get():
    """Lister tous les documents d'un utilisateur"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_get error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>", methods=["GET"])
def users_user_id_documents_document_id_get():
    """Récupérer les détails d'un document spécifique"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_get error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>", methods=["DELETE"])
def users_user_id_documents_document_id_delete():
    """Supprimer un document uploadé"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_delete error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/documents/<document_id>/status", methods=["PATCH"])
def users_user_id_documents_document_id_status_patch():
    """Mettre à jour le statut de validation d'un document"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"users_user_id_documents_document_id_status_patch error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/users/<user_id>/selfie", methods=["POST"])
def users_user_id_selfie_post():
    """Uploader le selfie de l'utilisateur pour vérification"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"users_user_id_selfie_post error: {e}")
        return jsonify({"error": str(e)}), 500

@documents_bp.route("/documents/types", methods=["GET"])
def documents_types_get():
    """Lister les types de documents acceptés (CNI, passeport, etc.)"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"documents_types_get error: {e}")
        return jsonify({"error": str(e)}), 500

