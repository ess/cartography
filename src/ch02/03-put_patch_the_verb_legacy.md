# PUT/PATCH: the Verb Legacy

While it's not strictly the case, `PUT` and `PATCH` are fairly often used interchangeably on REST APIs. Considering this, we're going to go ahead and implement these at the same time.

## Tests ##

Another fortunate bit is that `put` and `patch` have the same signature as `post`. That being the case, let's go ahead and copypasta the `post` test in `maury/tests/test_client.py` and modify it for our new methods:

```python
    @requests_mock.Mocker()
    def test_put(self, m):
        # The happy path
        m.put('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.put('sausages', None, None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.put(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.put('sausages', {'color' : 'gold'}, None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.put(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.put('ed209', None, None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.put(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.put('404', None, None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

    @requests_mock.Mocker()
    def test_patch(self, m):
        # The happy path
        m.patch('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.patch('sausages', None, None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.patch(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.patch('sausages', {'color' : 'gold'}, None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.patch(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.patch('ed209', None, None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.patch(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.patch('404', None, None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
```

As expected, these tests fail, as we don't yet have either the `put` or `patch` mehods in our client.

## Implementing the Methods ##

So, let's crack open `maury/client.py` again, copypasta the `post` method, and modify it to fit our new methods:

```python
    def put(self, path, params, data):
        """Perform an HTTP PUT on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        PUT data, send the request to the API and return the result.
        """

        r = requests.put(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = self.__headers)

        return self.__process_response(r)

    def patch(self, path, params, data):
        """Perform an HTTP PATCH on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        PATCH data, send the request to the API and return the result.
        """

        r = requests.patch(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = self.__headers)

        return self.__process_response(r)
```

With that, our tests pass, and we've now implemented 80% of the HTTP verbs that we need to meet our requirements. That means it's time to take another look and decide if we should refactor further.

## Refactoring: Reqeust Handler ##

It might seem obvious that since we've already made a common method to handle the processing of an API response that it would also make sense to break out a method that performs the requests in question.

That is a fine observation, and it is indeed what I would usually do myself. The problem here is that my lack of Python knowledge is preventing me from coming up with the best way to do so. So, I'm going to keep on going the way that we have been and leave this refactoring to you, if you choose to do it.
