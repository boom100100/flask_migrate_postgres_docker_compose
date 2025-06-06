from flask import jsonify
from flask.views import MethodView
from app.services.seed import SeedService


class SeedsView(MethodView):
    def get(self):
        response = jsonify({
            "result": "success",
            "code": 201,
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response