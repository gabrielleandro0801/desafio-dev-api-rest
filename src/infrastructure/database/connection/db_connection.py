from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
engine = create_engine('sqlite:///infrastructure/database/connection/database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def add_filters_in_query(query, model, **kwargs):
    for arg in kwargs:
        if kwargs[arg] is not None and arg not in ["page", "limit"]:
            attribute = getattr(model, arg, None)
            if attribute is not None:
                query = query.filter(attribute == kwargs[arg])
    return query
