# We Rent! Backend

This is the backend repository for the We Rent! application.

## Project Links

- **Backend Repository:** [Backend GitHub Repository](https://github.com/your-org/we-rent-backend)
- **Supabase:** [Supabase Project Link](https://app.supabase.io/project/your-project-id)
- **Koyeb:** [Koyeb Deployment Link](https://app.koyeb.com/app/your-app-id)
- **Frontend Repository:** [Frontend GitHub Repository](https://github.com/your-org/we-rent-frontend)
- **Frontend Deployment (Netlify):** [Netlify Deployment Link](https://your-frontend-site.netlify.app)

## Project Overview

The We Rent! backend is a RESTful API service built with Flask, designed to support the core functionalities of the We Rent! application. It manages user authentication, product listings, product details, reviews, and other business logic required for the rental platform.

## Codebase Structure

The repository is organized into the following key directories and files:

- `app.py`: The main application entry point where the Flask app is initialized.
- `config/`: Configuration files for different environments and settings.
- `models/`: Database models representing the core entities such as users, products, and reviews.
- `repo/`: Repository layer handling database operations and queries.
- `route/`: Flask route definitions organizing API endpoints by feature.
- `services/`: Business logic and service layer implementing core application functionality.
- `shared/`: Shared utilities and helper modules used across the codebase.
- `migrations/`: Database migration scripts managed by Flask-Migrate.
- `tests/`: Unit and integration tests to ensure code quality and correctness.
- `instance/`: Contains instance-specific files such as the database initialization.

## Development Process

The development process follows best practices for Python Flask applications, including:

- Use of virtual environments and dependency management via `uv` tool.
- Environment variable management through `.env` files to securely handle sensitive data.
- Containerized PostgreSQL database using Docker for consistent development environments.
- Database schema migrations managed with Flask-Migrate to handle incremental changes.
- Modular code organization separating concerns into models, repositories, routes, and services.
- Automated testing with `pytest` to maintain code reliability and facilitate continuous integration.

## Implementation Decisions

- **Flask Framework**: Chosen for its simplicity, flexibility, and strong ecosystem for building RESTful APIs.
- **PostgreSQL Database**: Selected for its robustness, scalability, and support for advanced SQL features.
- **Docker for Database**: Ensures consistent and isolated database environments across development machines.
- **Flask-Migrate**: Provides seamless database schema migrations aligned with SQLAlchemy models.
- **Environment Variables**: Used to keep sensitive information out of source control and enable easy configuration.
- **Layered Architecture**: Separates concerns into distinct layers (models, repositories, services, routes) to improve maintainability and testability.
- **Testing**: Emphasizes automated tests to catch regressions early and support agile development.

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

### 6. Running Tests

To execute the project's tests, use `uv` with `pytest`:

```bash
uv run pytest
```

The application should now be running and accessible, connecting to your PostgreSQL database using the environment variables.

## Contributing

Contributions to the We Rent! backend are welcome. Please follow the standard Git workflow:

- Fork the repository
- Create a feature branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Open a pull request for review

Ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
