# POST: the Reverbening #

Of course, our requirements state that we have to also be able to make `POST` requests to the API. So, we have more work cut out for us. Luckily, the handling of any given verb is quite a lot like the handling of any other given verb.

## A Note From Our Sponsors ##

Yeah, not really. More than anything, I wanted to take this opportunity to let you know that from this point on, listing the entirety of the referenced files would become unwieldy rather quickly.

So, from now on, I'll just show the changes in the code examples instead of the entire file, where possible.

## Test-Driven ##

Now that we're a little more familiar with the language and its unittest framework, let's change gears a bit. We're going to start our `POST` feature with a new test in `maury/tests/test_client.py`:

```python
    @requests_mock.Mocker()
    def test_post(self, m):
        # The happy path
        m.post('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.post('sausages', None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.post(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.post('sausages', {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.post(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.post('ed209', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.post(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.post('404', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
```

As you can see, our `post` test is almost identical to our `get` test. That's becuase, as mentioned above, all of the verbs are handled in more or less the same way. The big difference here is that `post` involves not just a path and a params dict, but also a dict of data to be `POST`ed to the endpoint.

After running our tests, we see that our `test_post` test yields an error. That's because we don't have a `post` method in our client yet. Let's do that.

## First Draft Implementation ##

Since they test the same (aside from the extra argument), it stands to reason that `get` and `post` should have rather similar implementations. Let's do a quick copypasta in `maury/client.py` and see how that works out:

```python
    def post(self, path, params, data):
        """Perform an HTTP POST on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        POST data, send the request to the API and return the result.
        """

        r = requests.post(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = {
                    'X-EY-TOKEN' : self.__token,
                    'accept' : 'application/vnd.engineyard.v3+json',
                    'content-type' : 'application/json',
                    })

        if r.ok:
            return Result(r.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % r.status_code
                )
```

Running our tests now yields a success:

```
test_post (maury.tests.test_client.TestResult) ... ok
```

So, one could argue that we're done at this point, but there's something that's bugging me a bit about this implementation. Take a look at the `get` and `post` methods. Notice how similar they are? We should probably take this opportunity to go ahead and refactor those similarities away.

## Refactoring: Response Processor ##

So, one of the things that makes these two methods so similar, aside from all verbs being very similar in the first place, is that they both interpret the API response identically. That being the case, we can construct a common method to use for response processing in `maury/client.py`:

```python
    def __process_response(self, response):
        """Process an API response into a Result."""

        if response.ok:
            return Result(response.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % response.status_code
                )

    def get(self, path, params):
        """Perform an HTTP GET on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.
        """

        r = requests.get(self.__construct_request_url(path),
                params = params,
                headers = {
                    'X-EY-TOKEN' : self.__token,
                    'accept' : 'application/vnd.engineyard.v3+json',
                    'content-type' : 'application/json',
                    })

        return self.__process_response(r)

    def post(self, path, params, data):
        """Perform an HTTP POST on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        POST data, send the request to the API and return the result.
        """

        r = requests.post(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = {
                    'X-EY-TOKEN' : self.__token,
                    'accept' : 'application/vnd.engineyard.v3+json',
                    'content-type' : 'application/json',
                    })

        return self.__process_response(r)
```

That's a little better, and thanks to our tests, we can see that the behavior has not changed. Yay TDD! Still, I see at least one more thing that I don't like: those repeated headers seem like a perfect aspect to reconsider.

## Refactoring: Headers ##

Now, there are a lot of ways that we could switch up the request headers dictionary. I usually go for a private method for things like this, but I'm also not familiar enough with Python to know how much of an impact on resource usage and performance constantly generating new dicts will have. That being the case, let's jump into `maury/client.py` and see if we can find another way:

```python
    def __init__(self, base_url, token):
        """Set the base_url and token for a new Client instance"""

        self.__base_url = base_url
        self.__headers = {
                'X-EY-Token' : token,
                'accept' : 'application/vnd.engineyard.com.v3+json',
                'content-type' : 'application/json'
                }

    def get(self, path, params):
        """Perform an HTTP GET on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.
        """

        r = requests.get(self.__construct_request_url(path),
                params = params,
                headers = self.__headers)

        return self.__process_response(r)

    def post(self, path, params, data):
        """Perform an HTTP POST on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        POST data, send the request to the API and return the result.
        """

        r = requests.post(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = self.__headers)

        return self.__process_response(r)
```

What we did there was to store the headers dictionary directly in the client object as `__headers`. Also, since we don't use the token for anything else, we are no longer storing the token at all. Also, the tests still pass, so it looks like we're still good.

## Refacotring: What's Next? ##

Can we go further? Sure, we can, but at this point, we probably shouldn't.

So far, all verb implementations have involved making an API request, then processing the API response. We have implemented less than half of the verbs that we have to implement, though.

That being the case, let's follow the advice that I'd imagine Sandy Metz would give right now: let's just keep working on the requirements until we're ***sure*** that we can safely refactor further.
