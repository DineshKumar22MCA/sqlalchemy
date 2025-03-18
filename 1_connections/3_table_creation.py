from sqlalchemy import Column, String, Integer, text
from sqlalchemy.orm import declarative_base

from connection import engine
from orm_connection import tables


try:
    Base = declarative_base()


    class User(Base):
        __tablename__ = "user"

        id = Column(Integer, primary_key=True)
        name = Column(String(255))

    Base.metadata.create_all(engine)

    #check tables
    if "user" in tables:
        print("table created successfully")
    else:
        print("table is not created")
    
    with engine.connect() as con:
        result = con.execute(text("show tables like 'user'"))
        table_exists = result.fetchone() is not None
        if table_exists:
            print("table created successfully")
        else:
            print("table is not created")

    if 'user' in Base.metadata.tables:
        print("table created")
    else:
        print("table not created")
except Exception as e:
    print(str(e))
    
