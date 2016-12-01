from test_base import BaseTestCase


class TestUsElectionsApi(BaseTestCase):

    def test_should_respond_ok_to_us_elections_path(self):
        response = self.client.get("/api/us_elections/")
        self.assert_200(response)
