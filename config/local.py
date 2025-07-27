import os

def _get_required_env(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' is not set.")
    return value

DB_USER = _get_required_env("DB_USER")
DB_PASSWORD = _get_required_env("DB_PASSWORD")
DB_HOST = _get_required_env("DB_HOST")
DB_PORT = int(_get_required_env("DB_PORT"))
DB_NAME = _get_required_env("DB_NAME")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# JWT configuration
JWT_SECRET_KEY = _get_required_env("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = int(_get_required_env("JWT_ACCESS_TOKEN_EXPIRES"))
