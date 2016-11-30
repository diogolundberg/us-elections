from flask import Blueprint, jsonify
from app.models.us_elections import USElections
from app import db

blueprint = Blueprint('us_elections_api', __name__, url_prefix='/api/us_elections')

@blueprint.route("/")
def list():
    election_results = db.session.query(USElections).all()
    return jsonify(data=[dict(n) for n in election_results])
