from test_base import BaseTestCase
from app.models.us_elections import USElections
from factories.us_elections_factory import USElectionsFactory

class TestUsElectionsApi(BaseTestCase):

    def setUp(self):
        USElectionsFactory.create_batch(10)

    def tearDown(self):
        USElections.query.delete()

    def test_api_should_return_10_us_elections(self):
        response = self.client.get("/api/us_elections/")
        self.assertEqual(len(response.json['data']), 10)
