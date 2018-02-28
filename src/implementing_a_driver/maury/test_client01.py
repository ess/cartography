from unittest import TestCase
import requests_mock

from maury.client import Client

class TestClient(TestCase):
    @requests_mock.Mocker()
    def test_get(self, m):
        # The happy path
        m.get('https://api.engineyard.com/sausages', text='gold')

        c = Client(token = 'faketoken')
        result = c.get('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, 'gold')

        # The happy path with params
        m.get('https://api.engineyard.com/sausages?color=gold', text='yep')

        result = c.get('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, 'yep')

        # A wild API error appears!
        m.get(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.get('ed209')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.get(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.get('404')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
