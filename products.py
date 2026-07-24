from flask import Blueprint, jsonify, request
from src.services.product_service import ProductService
from src.utils.validators import validate_product_payload

products_bp = Blueprint("products", __name__, url_prefix="/api/v1/products")
product_service = ProductService()

@products_bp.route("", methods=["GET"])
def list_products():
    products = product_service.get_all()
    return jsonify({
        "status": "success",
        "count": len(products),
        "data": products
    }), 200

@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = product_service.get_by_id(product_id)
    if not product:
        return jsonify({"status": "error", "message": "Product not found"}), 404
    return jsonify({"status": "success", "data": product}), 200

@products_bp.route("", methods=["POST"])
def add_product():
    data = request.get_json(silent=True)
    is_valid, error_message = validate_product_payload(data)
    
    if not is_valid:
        return jsonify({"status": "fail", "message": error_message}), 400
        
    created_product = product_service.create(data["name"], data["price"])
    return jsonify({
        "status": "success",
        "message": "Product created successfully",
        "data": created_product
    }), 201