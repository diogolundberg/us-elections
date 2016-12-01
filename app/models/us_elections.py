from sqlalchemy import Column, Integer, String, BigInteger
from app import db


class USElections(db.Model):
    __tablename__ = 'us_elections'

    id = Column(Integer, primary_key=True)
    county = Column(String)
    fips = Column(String)
    cand = Column(String)
    st = Column(String)
    votos = Column(BigInteger)
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

