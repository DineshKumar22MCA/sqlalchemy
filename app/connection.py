import os
from dotenv import load_dotenv

from sqlalchemy import create_engine


try:
    load_dotenv()

    DATABASE_HOST=os.getenv("DATABASE_HOST")
    DATABASE_USER=os.getenv("DATABASE_USER")
    DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
    DATABASE_DB=os.getenv("DATABASE_DB")

    DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}"

    engine = create_engine(DATABASE_URL)
    print(engine)
    print(type(engine))

    with engine.connect() as connection:
        print("database connected successfully")

except Exception as e:
    print(str(e))
