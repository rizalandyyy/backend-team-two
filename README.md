# We Rent! Backend

This is the backend repository for the We Rent! application.

## Project Links

- **Backend Repository:** [Backend GitHub Repository](https://github.com/rizalandyyy/backend-team-two)
- **Backend Deployment (Koyeb):** [Koyeb Deployment Link](https://indirect-yasmin-ananana-483e9951.koyeb.app/)
- **Postman API Documentation:** [Postman API Documentation](https://documenter.getpostman.com/view/44239234/2sB3B8st5c#1dff3df8-6ee7-4ed8-a064-0ea0660e3472)
- **Frontend Repository:** [Frontend GitHub Repository](https://github.com/ahmadhilmi420/werent-app)
- **Frontend Deployment (Vercel):** [Vercel Deployment Link](https://werent-app.vercel.app/products)

## Project Overview

The We Rent! backend is a RESTful API service built with Flask, designed to support the core functionalities of the We Rent! application. It manages user authentication, product listings, product details, reviews, and other business logic required for the rental platform.

## Database Schema

```plaintext
// User, Product, Product Detail and Review models

Table users {
  id integer [pk]
  username varchar [unique, not null]
  email varchar [unique, not null]
  password_hash varchar [not null]
  role enum [default: 'user', not null]
  created_at timestamp
  updated_at timestamp
}

Enum user_role {
  admin
  user
}

Table products {
  id integer [pk]
  name varchar [not null]
  price float [not null]
  condition varchar [not null] // e.g., new, used
  image_url varchar
  created_at timestamp
  updated_at timestamp
}

Table product_details {
  id integer [pk]
  product_id integer [not null, ref: > products.id]
  description text
  image1_url text
  image2_url text
  image3_url text
  created_at timestamp
  updated_at timestamp
}

Table reviews {
  id integer [pk]
  product_id integer [ref: > products.id, not null]
  user_id integer [ref: > users.id, not null]
  rating integer [not null]
  comment text
  created_at timestamp
  updated_at timestamp
}
```

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
- Database hosted on Supabase for managed PostgreSQL service.
- Database schema migrations managed with Flask-Migrate to handle incremental changes.
- Modular code organization separating concerns into models, repositories, routes, and services.
- Automated testing with `pytest` to maintain code reliability and facilitate continuous integration.

## Implementation Decisions

- **Flask Framework**: Chosen for its simplicity, flexibility, and strong ecosystem for building RESTful APIs.
- **Supabase Database**: Selected for its managed PostgreSQL service with additional features like authentication and real-time capabilities.
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
uv init
```

### 3. Environment Variables Setup

This project uses `.env` files to manage sensitive configuration data, such as database credentials and JWT secret keys.

1.  **Create your `.env` file**:
    Copy the provided example environment file to create your local configuration:

    ```bash
    cp .env.example .env
    ```

2.  **Edit `.env`**:
    Open the newly created `.env` file and replace the placeholder values with your actual Supabase database credentials and any other required secrets.

    Example (`.env` content):

    ```
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_KEY=your_supabase_anon_or_service_role_key

    JWT_SECRET_KEY=your_strong_jwt_secret_key
    JWT_ACCESS_TOKEN_EXPIRES=3600
    ```

    **Important**: **DO NOT** commit your `.env` file to version control. It is already included in `.gitignore`.

### 4. Database Setup

The project uses Supabase as the managed PostgreSQL database.

1.  **Create a Supabase project**:
    If you haven't already, create a new project on [Supabase](https://supabase.com/).

2.  **Configure your database**:
    Use the Supabase dashboard to manage your database schema or run migrations locally using Flask-Migrate.

3.  **Run Database Migrations**:
    Apply database migrations to create the necessary tables:

    ```bash
    uv run flask db upgrade
    ```

    Ensure your `.env` file contains the correct `SUPABASE_URL` and `SUPABASE_KEY` for the connection.

### 5. Start the Application Server

Once the dependencies are installed and the database is set up, you can start the Flask development server:

```bash
uv run task fr
```

Note: make sure taskipy is installed in your environment, and you have 'tool.taskipy.tasks' in your `pyproject.toml` file.

### 6. Deployment on Koyeb

To deploy the backend application on Koyeb, follow these steps:

1. Create an account and log in to [Koyeb](https://www.koyeb.com/).

2. Create a new app and connect your GitHub repository containing the backend code.

3. Configure environment variables in the Koyeb dashboard to match your `.env` file, including `SUPABASE_URL`, `SUPABASE_KEY`, `JWT_SECRET_KEY`, and others as needed.

4. Set the build and start commands:

   - Build command: `uv sync` (or your project's dependency installation command)
   - Start command: `uv run task fr`

5. Deploy the app and monitor the logs for successful startup.

### 7. Running Tests

To execute the project's tests, use `uv` with `pytest`:

```bash
uv run pytest -s -v
```

The application should now be running and accessible, connecting to your Supabase database using the environment variables.

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
