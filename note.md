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

```toml
[project]
name = "bumibrew"
version = "0.1.0"
description = "Sustainable market backend built with Flask"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "flask",
    "flask-sqlalchemy",
    "flask-jwt-extended",
    "flask-migrate",
    "sqlalchemy",
    "psycopg2-binary",
    "pytest",
    "pytest-cov",
    "black",
    "isort",
    "taskipy>=1.14.1",
    "flask-cors>=5.0.1",
    "marshmallow-sqlalchemy>=1.4.2",
    "python-dotenv>=1.1.0",
]
[tool.taskipy.tasks]
fr = "flask --app app run --port 8000 --reload --debug"
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

```
{
"username": "vendortest1",
"first_name": "Vendor1",
"last_name": "Test",
"email": "vendortest1@example.com",
"phone": "08110000001",
"password": "vendorpass123", / pass123
"date_of_birth": "1987-04-21",
"address": "Jl. Vendor No.1",
"city": "Bandung",
"state": "Jawa Barat",
"country": "Indonesia",
"zip_code": "40111",
"image_url": "http://example.com/vendor1.jpg",
"role": "vendor",
"bank_account": "111222333",
"bank_name": "Bank Mandiri"
}
{
"username": "customertest1",
"first_name": "Customer",
"last_name": "Test",
"email": "customertest1@example.com",
"phone": "08110000002",
"password": "customerpass123", / pass123
"date_of_birth": "1992-06-10",
"address": "Jl. Customer No.2",
"city": "Jakarta",
"state": "DKI Jakarta",
"country": "Indonesia",
"zip_code": "10110",
"image_url": "http://example.com/customer1.jpg",
"role": "customer",
"bank_account": "444555666",
"bank_name": "Bank BCA"
}
{
"username": "admintest1",
"first_name": "Admin",
"last_name": "Test",
"email": "admintest1@example.com",
"phone": "08110000003",
"password": "adminpass123", /pass123
"date_of_birth": "1980-01-01",
"address": "Jl. Admin No.3",
"city": "Surabaya",
"state": "Jawa Timur",
"country": "Indonesia",
"zip_code": "60222",
"image_url": "http://example.com/admin1.jpg",
"role": "admin",
"bank_account": "777888999",
"bank_name": "Bank BRI"
}
```

---

### Step 2: Deploy to Koyeb

To deploy the Flask application to Koyeb, follow these steps:

1. Ensure you have connected your Supabase database and set the necessary environment variables in Koyeb.

2. Add a `Procfile` to your project root with the following content to specify the run command for Koyeb:

```
web: gunicorn --bind 0.0.0.0:$PORT --workers 4 app:app
```

3. Build and push your Docker image to a container registry (e.g., Docker Hub):

```bash
docker build -t your-dockerhub-username/your-app-name:latest .
docker push your-dockerhub-username/your-app-name:latest
```

4. Create or update your Koyeb service to use the pushed Docker image.

5. Set the environment variables in your Koyeb service settings, including:

- `DATABASE_URL` or individual DB connection variables
- `JWT_SECRET_KEY`
- Supabase-related environment variables

6. Deploy the service and monitor the logs to ensure the app starts successfully.

For more details, refer to the [Koyeb documentation](https://koyeb.com/docs).

---
