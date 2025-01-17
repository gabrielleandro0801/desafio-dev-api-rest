from flask import Flask
from flask_restful import Api

import api.infrastructure.database.connection.db_connection as database
import api.infrastructure.middleware as middleware
import api.routes.v1.account_routes as v1_accounts
import api.routes.v1.transaction_routes as v1_transactions
import api.routes.v1.user_routes as v1_user
import api.routes.health_check_route as health_check

app: Flask = Flask(__name__)
api: Api = Api(app)

middleware.configure(app)
database.start_connection(app)

api = health_check.add_routes(api)
api = v1_user.add_routes(api)
api = v1_accounts.add_routes(api)
api = v1_transactions.add_routes(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)
