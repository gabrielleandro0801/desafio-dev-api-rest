from datetime import datetime
from http import HTTPStatus

from flask_restful import Resource


class HealthCheckController(Resource):

    def get(self):
        return {
            "message": "OK",
            "date": datetime.now().isoformat()
        }, HTTPStatus.OK
