from src.infrastructure.database.connection.db_connection import db, Base, add_filters_in_query
import src.domain.models.users as u


class Users(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    document = db.Column(db.String)

    @classmethod
    def find(cls, **kwargs) -> None or u.Users:
        query = db.session.query(Users)
        query = add_filters_in_query(query, Users, **kwargs)

        response = query.first()
        db.session.commit()

        return None if response is None \
            else u.Users(name=response.name, document=response.document)



