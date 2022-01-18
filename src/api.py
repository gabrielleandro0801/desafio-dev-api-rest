from flask import Flask
from flask_restful import Api

import src.infrastructure.database.connection.db_connection as database
import src.routes.v1.user_routes as v1_user_routes

app: Flask = Flask(__name__)
api: Api = Api(app)

# Configuring database
database.start_connection(app)

# Adding v1 routes
api = v1_user_routes.add_routes(api)

if __name__ == '__main__':
    app.run()

# Subir docker-compose up -d
