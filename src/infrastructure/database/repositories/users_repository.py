from flask_sqlalchemy import BaseQuery

from src.infrastructure.database.connection.db_connection import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column('id', db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100), nullable=False)
    document = db.Column('document', db.String(14), unique=True, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.document = kwargs.get('document')


class UsersRepository:
    def __init__(self) -> None:
        pass

    def find_by_user_id(self, user_id: int) -> Users or None:
        query: BaseQuery = Users.query.filter(Users.id == user_id)
        user = query.first()
        db.session.commit()
        return user

    def find_by_document(self, document: str) -> Users or None:
        query = Users.query.filter(Users.document == document)
        user: Users or None = query.first()
        db.session.commit()
        return user

    def save(self, user: Users):
        db.session.add(user)
        db.session.commit()
        return user

    def delete_by_user_id(self, user: Users):
        db.session.delete(user)
        db.session.commit()
