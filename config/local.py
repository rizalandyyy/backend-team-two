# DB_HOST = "localhost"
# DB_NAME = "werent_db"
# SQLALCHEMY_DATABASE_URI = "sqlite:///local.db"


DB_USER = "postgres.rxpgseukvaxcdcddsmup"
DB_PASSWORD = "wPVtHFxsMT2PVQiE"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = 5432
DB_NAME = "postgres"
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# postgresql://postgres.rxpgseukvaxcdcddsmup:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres

# JWT configuration
JWT_SECRET_KEY = "ouWyAUOsc4NRTfPzgpMv"
JWT_ACCESS_TOKEN_EXPIRES = 3600
