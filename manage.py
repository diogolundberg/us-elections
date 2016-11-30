from flask import Flask, jsonify, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, BigInteger
import pandas
import math

flask = Flask(__name__)
flask.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///us_elections'

db = SQLAlchemy(flask)
manager = Manager(flask)

class USElections(db.Model):
    __tablename__ = 'us_elections'

    id = Column(Integer, primary_key=True)
    county = Column(String)
    fips = Column(String)
    cand = Column(String)
    st = Column(String)
    votes = Column(BigInteger)
    total_votes = Column(BigInteger)
    lead = Column(String)

    def __iter__(self):
        yield 'county', self.county
        yield 'fips', self.fips
        yield 'cand', self.cand
        yield 'st', self.st
        yield 'votes', self.votes
        yield 'total_votes', self.total_votes
        yield 'lead', self.lead


@manager.command
def load_data():
    def handle_na(data):
        return 0 if math.isnan(float(data)) or data == 'NA' else int(data)

    data_frame = pandas.read_csv('data/pres16results.csv')

    for index, row in data_frame.iterrows():
        us_elections = USElections()
        us_elections.county = str(row['county'])
        us_elections.fips = str(row['fips'])
        us_elections.cand = str(row['cand'])
        us_elections.st = str(row['st'])
        us_elections.votes = handle_na(row['votes'])
        us_elections.total_votes = handle_na(row['total_votes'])
        us_elections.lead = str(row['lead'])
        db.session.add(us_elections)

    db.session.commit()

@flask.route("/json")
def json():
    election_results = db.session.query(USElections).all()
    return jsonify(data=[list(dict(n).values()) for n in election_results])

@flask.route("/")   
def index():
    return render_template('index.html')

manager.run()
