from flask import jsonify
from flask.views import MethodView
from sqlalchemy.sql import text

from app.database import db

class SeedsView(MethodView):
    def get(self):
        try:
            # quick check: flask db upgrade ran successfully, so the users table should exist.
            db.session.execute(text("SELECT id FROM users LIMIT 1;"))
            response = jsonify({
                "result": "success",
                "code": 201,
            })
        except:
            response = jsonify({
            "result": "failed",
            "code": 500,
        })

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response