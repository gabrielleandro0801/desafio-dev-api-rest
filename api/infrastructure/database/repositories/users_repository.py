from flask_sqlalchemy import BaseQuery

from api.domain.models.user import User
from api.infrastructure.database.connection.db_connection import db


class UsersRepository:

    @classmethod
    def find_by_user_id(cls, user_id: int) -> User or None:
        query: BaseQuery = User.query.filter(User.id == user_id)
        user: User or None = query.first()
        return user

    @classmethod
    def find_by_document(cls, document: str) -> User or None:
        query = User.query.filter(User.document == document)
        user: User or None = query.first()
        return user

    @classmethod
    def save(cls, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete(cls, user: User) -> None:
        db.session.delete(user)
        db.session.commit()
