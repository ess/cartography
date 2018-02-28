from unittest import TestCase
import requests_mock

from maury.client import Client

class TestClient(TestCase):
    @requests_mock.Mocker()
    def test_get(self, m):
        # The happy path
        m.get('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client(token = 'faketoken')
        result = c.get('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.get(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.get('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

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

    @requests_mock.Mocker()
    def test_post(self, m):
        # The happy path
        m.post('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client(token = 'faketoken')
        result = c.post('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.post(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.post('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.post(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.post('ed209')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.post(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.post('404')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

    @requests_mock.Mocker()
    def test_put(self, m):
        # The happy path
        m.put('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client(token = 'faketoken')
        result = c.put('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.put(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.put('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.put(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.put('ed209')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.put(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.put('404')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

    @requests_mock.Mocker()
    def test_patch(self, m):
        # The happy path
        m.patch('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client(token = 'faketoken')
        result = c.patch('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.patch(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.patch('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.patch(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.patch('ed209')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.patch(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.patch('404')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

    @requests_mock.Mocker()
    def test_delete(self, m):
        # The happy path
        m.delete('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client(token = 'faketoken')
        result = c.delete('sausages')
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.delete(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.delete('sausages', params = {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.delete(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.delete('ed209')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.delete(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.delete('404')
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

