from flask_sqlalchemy import BaseQuery

from src.infrastructure.database.connection.db_connection import db, Base


class Users(Base):
    __tablename__ = "users"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    document = db.Column('document', db.String)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.document = kwargs.get('document')


class UsersRepository:
    def __init__(self) -> None:
        pass

    def find_by_document(self, document: str) -> None or Users:
        query: BaseQuery = db.session.query(Users)
        query = query.filter(Users.document == document)

        response: Users or None = query.first()
        db.session.commit()

        # return None if response is None else self.__translator.translate_response_to_model(response)
        return response

    # @classmethod
    # def save(cls, user: u.Users):
    #     model = Users(user)
    #     db.session.add(model)
    #     db.session.commit()
    #     print(model)
