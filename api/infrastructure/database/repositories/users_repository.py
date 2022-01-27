from flask_sqlalchemy import BaseQuery

from api.domain.models.users import Users
from api.infrastructure.database.connection.db_connection import db


class UsersRepository:

    @classmethod
    def find_by_user_id(cls, user_id: int) -> Users or None:
        query: BaseQuery = Users.query.filter(Users.id == user_id)
        user = query.first()
        db.session.commit()
        return user

    @classmethod
    def find_by_document(cls, document: str) -> Users or None:
        query = Users.query.filter(Users.document == document)
        user: Users or None = query.first()
        db.session.commit()
        return user

    @classmethod
    def save(cls, user: Users) -> Users:
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete(cls, user: Users) -> None:
        db.session.delete(user)
        db.session.commit()
