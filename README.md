# We Rent! Backend
This is the backend repository for the We Rent! application.

## Getting Started

Follow these steps to set up and run the backend locally.

### 1. Clone the Repository

```bash
git clone <repo-url>
cd we-rent-backend
```

### 2. Install Dependencies

Ensure you have `uv` installed (`pip install uv`). Then synchronize dependencies:

```bash
uv sync
```

### 3. Environment Variables Setup

This project uses `.env` files to manage sensitive configuration data, such as database credentials and JWT secret keys.

1.  **Create your `.env` file**:
    Copy the provided example environment file to create your local configuration:
    ```bash
    cp .env.example .env
    ```

2.  **Edit `.env`**:
    Open the newly created `.env` file and replace the placeholder values with your actual database credentials and any other required secrets.

    Example (`.env` content):
    ```
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost # or your database host if external
    DB_PORT=5432
    DB_NAME=WeRent_db

    JWT_SECRET_KEY=your_strong_jwt_secret_key
    JWT_ACCESS_TOKEN_EXPIRES=3600
    ```
    **Important**: **DO NOT** commit your `.env` file to version control. It is already included in `.gitignore`.

### 4. Database Setup

The project uses PostgreSQL with Docker for the database.

1.  **Start the database container**:
    Ensure your Docker daemon is running, then spin up the PostgreSQL database service:
    ```bash
    docker compose up -d db-postgres
    ```
    This will start the PostgreSQL container. The database service `db-postgres` is configured to read `POSTGRES_USER` and `POSTGRES_PASSWORD` from your `.env` file.

2.  **Run Database Migrations**:
    If this is your first time setting up the database, or if there are new model changes, you need to apply database migrations to create the necessary tables.
    ```bash
    uv run flask db upgrade
    ```
    This command will apply any pending database schema changes using Flask-Migrate. Ensure your `db-postgres` container is running before executing this.

### 5. Start the Application Server

Once the dependencies are installed and the database is set up, you can start the Flask development server:

```bash
uv run task fr
```

The application should now be running and accessible, connecting to your PostgreSQL database using the environment variables.