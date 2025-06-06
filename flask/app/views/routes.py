from flask import Blueprint
from app.views.seeds import SeedsView
# from app.views import CoachesView, MeetingsView, SeedsView, StudentsView


app_blueprint = Blueprint('app', __name__)
api_v1_blueprint = Blueprint('api_v1', __name__)

api_v1_blueprint.add_url_rule("/seeds", view_func=SeedsView.as_view("seeds"), methods=['GET',])
