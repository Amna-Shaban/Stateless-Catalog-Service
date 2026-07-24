@health_bp.route("/health", methods=["GET"])
def check_health():
    return jsonify({
        "status": "healthy",
        "service": "YOUR_NEW_PROJECT_NAME",  # <-- Change here
        "version": "1.0.0"
    }), 200