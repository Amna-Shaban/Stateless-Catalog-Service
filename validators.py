def validate_product_payload(data):
    if not data or not isinstance(data, dict):
        return False, "Invalid JSON body provided."
    
    if "name" not in data or not isinstance(data["name"], str):
        return False, "Field 'name' is required and must be a string."
        
    if "price" not in data or not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return False, "Field 'price' is required and must be a non-negative number."
        
    return True, None