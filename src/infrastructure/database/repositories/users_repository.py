from flask_sqlalchemy import BaseQuery

import src.domain.models.users as u
from src.infrastructure.database.connection.db_connection import db


class UsersRepository:

    @classmethod
    def find_by_user_id(cls, user_id: int) -> u.Users or None:
        query: BaseQuery = u.Users.query.filter(u.Users.id == user_id)
        user = query.first()
        db.session.commit()
        return user

    @classmethod
    def find_by_document(cls, document: str) -> u.Users or None:
        query = u.Users.query.filter(u.Users.document == document)
        user: u.Users or None = query.first()
        db.session.commit()
        return user

    @classmethod
    def save(cls, user: u.Users) -> u.Users:
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete(cls, user: u.Users) -> None:
        db.session.delete(user)
        db.session.commit()
