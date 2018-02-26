# DELETE: the Final Verb #

Our driver is very nearly complete. We only have one verb left to go, so let's get to it!

## Test ##

As it would happen, `delete` has the same signature and expectations as `get`, so let's go ahead and copypasta `test_get` and modify it to `test_delete` in `maury/tests/test_client.py`:

```python
@requests_mock.Mocker()
    def test_delete(self, m):
        # The happy path
        m.delete('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.delete('sausages', None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.delete(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.delete('sausages', {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.delete(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.delete('ed209', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.delete(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.delete('404', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
```

Okay, we have a failing test now, so we're going to do the obvious.

## Implementing DELETE ##

Since the signature is the same as `get`, we're going to copypasta the `get` method definition and modify it to fit our new `delete` method in `maury/client.py`:

```python
    def delete(self, path, params):
        """Perform an HTTP DELETE on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.
        """

        r = requests.delete(self.__construct_request_url(path),
                params = params,
                headers = self.__headers)

        return self.__process_response(r)
```

There we have it. Now that all of the defined requirements are met and all of our tests pass, our client driver is technically complete.
