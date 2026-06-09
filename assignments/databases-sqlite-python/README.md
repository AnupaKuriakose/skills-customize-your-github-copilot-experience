# 📘 Assignment: Databases & Persistence — SQLite with Python

## 🎯 Objective

Learn how to persist data using SQLite from Python. You'll design a small schema, perform CRUD operations with the `sqlite3` module, and integrate persistence into a simple application.

## 📝 Tasks

### 🛠️	Design schema and implement CRUD functions

#### Description
Create a SQLite database and implement Python functions to create, read, update, and delete records for a simple resource (e.g., `Note` or `Item`). Use parameterized queries and basic transactions where appropriate.

#### Requirements
Completed project should:

- Create a SQLite database file and a table with appropriate columns (e.g., `id`, `title`, `content`, `created_at`).
- Provide Python functions or a small module with `create`, `list`, `get`, `update`, and `delete` operations.
- Use parameterized queries to avoid SQL injection.
- Handle errors gracefully and close connections properly.
- Include example usage or a small CLI script demonstrating the operations.

Example usage:
```
python starter_code.py --init-db
python starter_code.py --add "Buy milk" "Remember to buy milk"
python starter_code.py --list
```

### 🛠️	Optional: Integrate with a web API or ORM

#### Description
Extend the assignment by connecting persistence to a small web API (FastAPI) or refactor to use `SQLAlchemy` for higher-level abstractions.

#### Requirements
Completed project may (optional):

- Add a FastAPI layer that exposes CRUD endpoints backed by the SQLite store.
- Use `SQLAlchemy` models and migrations for schema management.
- Add tests verifying database operations using temporary databases.
- Provide a `Dockerfile` or notes for deploying with a persistent volume.

---

Starter code and a `requirements.txt` are included. Run the starter CLI to initialize the database and try basic operations.

```
python starter_code.py --help
```
