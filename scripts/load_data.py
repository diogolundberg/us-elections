import pandas
import math
from flask_script import Command
from app.models.us_elections import USElections
from app import db


class LoadData(Command):

    "Loads elections data"

    def run(self):
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
