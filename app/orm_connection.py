from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, inspect, MetaData

from connection import engine


try:
    SessionLocal = sessionmaker(bind=engine)
    print(SessionLocal)
    print(type(SessionLocal))

    session = SessionLocal()
    print(session)
    print(type(session))

    if session.bind:
        print("database session connected")    
    
    if session.is_active:
        print("session is active")

    if session.execute(text("select 1")):
        print(session.execute(text("select 1")))

    # tables = engine.table_names()
    # print(tables)

    inspects = inspect(engine)

    tables = inspects.get_table_names()
    print(tables)

    metadata = MetaData()
    metadata.reflect(bind=engine)
    tables_list = list(metadata.tables.keys())
    print(tables_list)

except Exception as e:
    print(str(e))
    