import factory
from app import db
from app.models.us_elections import USElections


class USElectionsFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = USElections
        sqlalchemy_session = db.session
    
    county = 'adsasd'
    fips = 'adsasd'
    cand = 'adsasd'
    st = 'adsasd'
    votes = 213132
    total_votes = 231
    lead = 'adsasd'