from flask import Flask
from flask_restful import Api

import api.infrastructure.database.connection.db_connection as database
import api.routes.v1.accounts_routes as v1_accounts
import api.routes.v1.transactions_routes as v1_transactions
import api.routes.v1.user_routes as v1_user

app: Flask = Flask(__name__)
api: Api = Api(app)

database.start_connection(app)

api = v1_user.add_routes(api)
api = v1_accounts.add_routes(api)
api = v1_transactions.add_routes(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
