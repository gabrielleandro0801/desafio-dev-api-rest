from flask import Flask
from flask_restful import Api

import src.infrastructure.database.connection.db_connection as database
import routes.v1.user_routes as v1_user_routes

app: Flask = Flask(__name__)
api: Api = Api(app)

# Configuring database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///infrastructure/database/connection/database.db'
database.db.init_app(app)

# Adding v1 routes
api = v1_user_routes.add_routes(api)

if __name__ == '__main__':
    app.run()
