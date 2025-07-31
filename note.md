### 1. Initialize Project

```bash
uv init
```

### 2. Add Dependencies

```bash
uv add flask                # web framework
uv add pytest               # for testing

uv add flask-migrate        # DB migrations
uv add flask-sqlalchemy     # ORM
uv add psycopg2-binary      # DB driver

uv add flask-jwt-extended   # for authentication
uv add pydantic             # for data validation
uv add python-dotenv        # for environment variables
uv add taskipy              # for task automation
uv add flask-cors           # for frontend-backend integration
uv add marshmallow-sqlalchemy # for data validation
uv add marshmallow           # for data validation
uv export > requirements.txt  # export to requirements.txt
uv add Flask-Limiter        # for rate limiting
uv add redis                # for caching
uv remove marshmallow-sqlalchemy           # remove marshmallow-sqlalchemy

```

```txt
gunicorn==21.2.0 \
    --hash=sha256:3213aa5e8c24949e792bcacfc176fef362e7aac80b76c56f6b5122bf350722f0

```

```toml
    [tool.taskipy.tasks]
    fr = "flask --app app run --port 8000 --reload --debug"
```

### Run server:

```bash
uv run task fr
```

### 3. Run Tests (Optional)

```bash
uv run pytest -s -v
```

### 4. Set Up Database Migrations

```bash
uv run flask db init
uv run flask db migrate -m "Initial migration"
uv run flask db upgrade
```

### 5. Flask App Directory Structure

```bash
.
├── instance/                # Environment-specific configs (e.g., secrets, DB URIs)
├── middlewares/            # Custom middleware (auth decorators, error handling, etc.)
├── models/                 # SQLAlchemy database models (User, Product, Order, etc.)
├── repo/                   # Repository layer for DB queries (separates logic from routes)
├── route/                  # Flask Blueprints (auth, product, cart, order endpoints)
├── shared/                 # Utility functions, constants, reusable services
├── tests/                  # Pytest-based unit/integration tests
├── config/                 # App configuration (dev, prod, default settings)
│
├── app.py                  # Main app entrypoint and app factory
├── conftest.py             # Global test fixtures for pytest
├── pyproject.toml          # Project metadata and dependencies (used by `uv`)
├── README.md               # Project documentation and setup instructions
└── uv.lock                 # Locked dependencies for reproducibility
```
