# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Magic card collection management REST API built with FastAPI. Users authenticate via JWT and can manage collections of Magic: The Gathering cards.

## Commands

```bash
# Install dependencies
pip install -r requirement.txt

# Run the dev server
fastapi dev main.py
# or
uvicorn main:app --reload

# Run all tests
pytest

# Run a single test file
pytest tests/auth/test_register.py

# Run a specific test
pytest tests/auth/test_register.py::test_register_new
```

## Architecture

**Entry point:** `main.py` — creates the FastAPI app and mounts routers.

**Routers** (`router/`): Each file defines an `APIRouter` with a prefix and is included in `main.py`.
- `auth.py` — `/auth` prefix: login, register, refresh, logout
- `cards.py` — `/cards` prefix: card search and detail
- `collections.py` — `/collections` prefix: CRUD on user collections

**Services** (`services/`): Business logic layer consumed by routers via FastAPI `Depends()`.
- `auth_service.py` — token decoding and `get_current_user` dependency

**Schemas** (`schemas/`): Pydantic models for request/response validation.
- `user.py` — `User` model (`full_name`, `email`, `hashed_password`)
- `login_info.py` — `LoginInfo` model (`username`, `password`)

**Tests** (`tests/`): Organized by feature (e.g. `tests/auth/`). Async tests are supported via `pytest-asyncio` with `asyncio_mode = auto` (configured in `pytest.ini`). Use `httpx` for HTTP-level integration tests.

## Planned stack (from README)

- PostgreSQL + SQLAlchemy + Alembic (migrations)
- PyJWT for token handling
- Docker + GitHub Actions CI/CD
- Deployment on company VPS

## Planned data models

| Table | Key fields |
|---|---|
| `users` | id, full_name, email, hashed_password, created_at |
| `cartes` | id, name, edition, rarity, foil, language, image, text, strength, endurance, created_at |
| `collections` | id, name, type (enum: batch/deck/…), created_at, user_id |
| `collection_carte` | id, carte_id, collection_id, card_quantity |
| `audit_logs` | id, entity_type, entity_id, old_value, new_value, user_id, created_at |
