from api.infrastructure.database.connection.db_connection import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column('id', db.Integer, unique=True, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    document = db.Column('document', db.String(14), unique=True, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.document = kwargs.get('document')
