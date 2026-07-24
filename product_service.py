from src.utils.logger import setup_logger

logger = setup_logger()

class ProductService:
    def __init__(self):
        # In-memory database
        self._db = [
            {"id": 1, "name": "Laptop", "price": 999.00, "in_stock": True},
            {"id": 2, "name": "AirPods", "price": 150.00, "in_stock": True}
        ]

    def get_all(self):
        return self._db

    def get_by_id(self, product_id):
        return next((p for p in self._db if p["id"] == product_id), None)

    def create(self, name, price):
        new_id = len(self._db) + 1
        new_product = {
            "id": new_id,
            "name": name,
            "price": float(price),
            "in_stock": True
        }
        self._db.append(new_product)
        logger.info(f"Product created: ID {new_id} - {name}")
        return new_product