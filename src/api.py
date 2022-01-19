import flask as f
import flask_restful as fr

import src.infrastructure.database.connection.db_connection as database
import src.routes.v1.user_routes as v1_user_routes

app: f.Flask = f.Flask(__name__)
api: fr.Api = fr.Api(app)

database.start_connection(app)

# Adding v1 routes
api = v1_user_routes.add_routes(api)

if __name__ == '__main__':
    app.run()

# Subir docker-compose up -d
