from flask_sqlalchemy import BaseQuery

import src.domain.models.users as u
from src.infrastructure.database.connection.db_connection import db


class UsersRepository:
    def __init__(self) -> None:
        pass

    def find_by_user_id(self, user_id: int) -> u.Users or None:
        query: BaseQuery = u.Users.query.filter(u.Users.id == user_id)
        user = query.first()
        db.session.commit()
        return user

    def find_by_document(self, document: str) -> u.Users or None:
        query = u.Users.query.filter(u.Users.document == document)
        user: u.Users or None = query.first()
        db.session.commit()
        return user

    def save(self, user: u.Users) -> u.Users:
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user: u.Users) -> None:
        db.session.delete(user)
        db.session.commit()
