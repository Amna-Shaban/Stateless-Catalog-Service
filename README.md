# ⚡ Stateless Catalog Service

A modular, lightweight RESTful web server built with Python and Flask. Designed around clean architecture principles, this service decouples route management, business logic, validation, and presentation.

---

## 🏗️ Architectural Highlights

* **Application Factory Pattern:** Uses `create_app()` for flexible app setup and testing configuration.
* **Modular Routing (Blueprints):** Clean separation of API routes (`/api/v1/products`), system health check (`/health`), and UI presentation routes.
* **Service Layer Pattern:** Business logic is encapsulated inside `ProductService`, separating data manipulation from HTTP handling.
* **Request Validation & Structured Logging:** Centralized validation utility (`validators.py`) and custom logging (`logger.py`) to handle incoming payload errors gracefully.
* **Integrated Frontend Dashboard:** Simple HTML/JS interface serving interactive product catalog requests in real-time.

---

## 🛠️ Project Structure

```text
├── app.py                  # Entry point
└── src/
    ├── __init__.py         # App factory & blueprint registration
    ├── routes/
    │   ├── products.py     # Product API endpoints
    │   ├── health.py       # Health check endpoint
    │   └── frontend.py     # Dashboard presentation route
    ├── services/
    │   └── product_service.py # Core business logic
    ├── utils/
    │   ├── validators.py   # Request body validation
    │   └── logger.py       # Terminal logging formatter
    └── templates/
        └── index.html      # Lightweight frontend UI
```
## 🚀 API Endpoints

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Serves the interactive frontend dashboard | `200 OK` |
| **GET** | `/health` | System health check and service details | `200 OK` |
| **GET** | `/api/v1/products` | Retrieve all items from the inventory catalog | `200 OK` |
| **GET** | `/api/v1/products/<id>` | Fetch specific product details by product ID | `200 OK` / `404 Not Found` |
| **POST** | `/api/v1/products` | Add a new product to the catalog | `201 Created` / `400 Bad Request` |

---

### 📝 Request & Response Examples

#### 1. System Health Check
* **Request:** `GET /health`
* **Response:**
```json
{
  "service": "decodelabs_project1",
  "status": "healthy",
  "version": "1.0.0"
}
````
#### 2. Get Single Product
* **Request:** `GET /api/v1/products/1`
* **Response:**
```json
{
  "data": {
    "id": 1,
    "in_stock": true,
    "name": "Laptop",
    "price": 999.0
  },
  "status": "success"
}
````
#### Add New Product

* **Endpoint:** `POST /api/v1/products`
* **Headers:** `Content-Type: application/json`

**Request Body Example:**
```json
{
  "name": "USB Drive",
  "price": 20.00
}

