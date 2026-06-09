# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to design and implement a small REST API using FastAPI. You'll practice defining routes, request/response models with Pydantic, and running the app with Uvicorn.

## 📝 Tasks

### 🛠️	Implement a basic REST API

#### Description
Create a small FastAPI application that exposes CRUD-style endpoints for a simple resource (e.g., `Item`). Implement request validation using Pydantic models and return appropriate HTTP status codes.

#### Requirements
Completed project should:

- Provide a running FastAPI app (e.g., `uvicorn starter_code:app --reload`).
- Implement at least the following endpoints:
  - `GET /items/` — list items
  - `GET /items/{id}` — retrieve a single item
  - `POST /items/` — create an item (validate request body)
  - `PUT /items/{id}` — update an item
  - `DELETE /items/{id}` — delete an item
- Use Pydantic models for request and response schemas.
- Return appropriate HTTP status codes (201 for creation, 404 for not found, etc.).
- Include example curl commands or sample requests in the README.

Example curl snippet:
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"Book","price":12.5}' http://localhost:8000/items/
```

### 🛠️	Optional: Enhancements

#### Description
Add features that demonstrate deeper FastAPI usage or deployment readiness.

#### Requirements
Completed project may (optional):

- Persist data to a simple in-memory store or a file-based JSON store.
- Add query parameters for filtering or pagination on `GET /items/`.
- Include request authentication (API key) for protected endpoints.
- Add automated tests using `pytest` and the `TestClient` from `fastapi`.
- Provide a `Dockerfile` or deployment notes for running on a server.

---

Starter code and `requirements.txt` are included in this folder to help you get started. Run the app with:

```
pip install -r requirements.txt
uvicorn starter_code:app --reload
```

If you want, I can extend the starter code with tests or a Dockerfile—tell me which.
