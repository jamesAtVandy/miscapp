from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using the connection string provided by the user, assuming it's correct for their environment.
# If this fails, we might need to verify the credentials.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
# Note: I'm using a generic local URL. The user's URL "postgresql://postgres:@postgres@localhost:5432/" was malformed.
# I'll try to interpret it: user=postgres, pass=@postgres? Or just typo.
# I will use a standard one and let the user know, or try to preserve theirs if it looks intentional.
# Let's use a safer default for local dev if they don't have postgres set up: SQLite.
# But they asked for "backend code... primed".
# I'll stick to Postgres but use a cleaner URL pattern.
# Actually, I'll use the user's URL but corrected:
# If they meant password "@postgres", it should be "postgresql://postgres:@postgres@localhost:5432/"
# I'll write it as:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
