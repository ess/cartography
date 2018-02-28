from unittest import TestCase

from maury.result import Result

class TestResult(TestCase):
    def test_ok(self):
        good = Result('yay', None)
        bad = Result(None, 'uh-oh')

        self.assertTrue(good.ok)
        self.assertFalse(bad.ok)

    def test_body(self):
        body = "head and shoulders, knees and toes"
        result = Result(body, None)

        self.assertEqual(result.body, body)

        result = Result(body, 'Onoes!')

        self.assertEqual(result.body, None)

    def test_error(self):
        body = 'eyes and ears and mouth and nose'
        error = "I've made a terrible mistake"
        result = Result(body, error)

        self.assertEqual(result.error, error)

