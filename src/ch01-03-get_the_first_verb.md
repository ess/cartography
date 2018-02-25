# GET: the First Verb #

I like to start my implementation with the first, least-destructive HTTP verb in mind: `GET`.

So, let's get started developing our `Client` class. Why am I using a class here? Aside from the general *when in Rome ...* rule (though I'm told that it's almost bad form to do OOP in this OO language, by somebody who's probably trollin'), I have some plans down the line for how this client will be used. Also, our requirements flat out state that we need to keep track of some data: the base URL for the API and an authentication token.

Let's start there! In `maury/client.py`, we'll put the following:

```python
class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url = 'https://api.engineyard.com', token = None):
        """Set up a Client instance

        Positional arguments:
        base_url -- the base URL of the API (default: 'https://api.engineyard.com')
        token -- the API authentication token (default: None)
        """

        self.__base_url = base_url
        self.__token = token
```

There we go. We now have a `Client` class that accepts a base URL and a token. Our work is done!

## Constructing URLs ##

Dangit. Okay. More work it is.

Our requirements say that we need to be able to construct URLs based off of a relative endpoint path. So, let's do that in `maury/client.py`, too:

```python
from furl import furl

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set up a Client instance

        Positional arguments:
        base_url -- the base URL of the API
        token -- the API authentication token
        """

        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url
```

Well, that was easy. That's two requirements down ... let's go for a third.

## Speaking HTTP ##

We need to be able to speak HTTP! Back to `maury/client.py`:

```python
from furl import furl
import requests

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set up a Client instance

        Positional arguments:
        base_url -- the base URL of the API
        token -- the API authentication token
        """


        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url
```

It's almost cheating, but simply importing the `requests` package means that we can speak HTTP in this module. Moving on ...

## HTTP GET ##

This might be the most complicated requirement that we've tackled so far, and it's not the lowest-hanging fruit on the list of remaining requirements, but it makes sense to do this next because of reasons.

So, let's implement the first public method in our `Client` class: `get`:


```python
from furl import furl
import requests

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set up a Client instance

        Positional arguments:
        base_url -- the base URL of the API
        token -- the API authentication token
        """


        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url

    def get(self, path, params):
        """Perform an HTTP GET on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.
        """

        r = requests.get(self.__construct_request_url(path),
                params=params)

        return response.text
```

That's fine and good, and it technically fulfills the `implements HTTP GET` requirement, but there are a few problems with this implementation:

* It won't work: his is an authenticated API, but we're not handling authentication
* It might not work: we haven't specified an API version
* It might not work: we are assuming that the API is always in top notch operational condition and that we are always sending a valid request ... there is no error handling at all

Let's fix those in that order.

## Authentication ##

So, in order to provide our authentication token to the API, we either have to pass it in as part of the query string, or we have to set the `X-EY-TOKEN` header. Between the two of these, the header option is more secure and just plain less messy, so let's do that.


```python
from furl import furl
import requests

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set the base_url and token for a new Client instance"""

        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url

    def get(self, path, params):
        """Perform an HTTP GET on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.
        """

        r = requests.get(self.__construct_request_url(path),
                params = params,
                headers = {'X-EY-TOKEN' : self.__token})

        return response.text
```

That's taken care of. Next up is to specify the API version.

## API Version ##

In order to specify the version of the API that we want to use, we have to pass it in as part of the `Accept` header.

```python
from furl import furl
import requests

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set the base_url and token for a new Client instance"""

        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url

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
                    })

        return response.text
```

We specified the heck out of that API version, I reckon. One more to go!

## API Error Handling ##

This one might seem a bit weird if you're actually familiar with Python, but since I'm not particularly, I'm going to do the thing that makes the most sense to me, heavily influenced by other languages that I know better.

You see, the thing here is that I don't actually know much about how to handle exceptions in Python, and I actually don't like using exceptions for error handling. Some of my favorite languages use some form of multiple return for error handling. While I could do that with a `list` or a `tuple`, there's a technique that I prefer: let's make a `Result` class in `maury/result.py`:

```python
class Result(object):
    """The result of an operation.

    A result has two parts: a body, and an error.
    If the result contains an error, things are not ok.
    If the result contains no error, things are ok.
    """

    def __init__(self, body, error):
        """Set up a new Result.

        Positional arguments:
        body -- the content to pass along if things are ok
        error -- the content to pass along if things are not ok
        """

        self.__body = body
        self.__error = error

    @property
    def ok(self):
        """Are things ok?

        If the result has an error, this is false. Otherwise, true.
        """

        return self.__error == None

    @property
    def body(self):
        """The positive result content"""

        if self.ok:
            return self.__body

        return None

    @property
    def error(self):
        """The negative result content"""
        return self.__error
```

Now that we have a way to express both positive and negative results, let's tie it in and use it in our `Client`:

```python
from furl import furl
import requests
from .result import Result

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set the base_url and token for a new Client instance"""

        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url

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
                    })

        if r.ok:
            return Result(r.text, None)

        return Result(
                None,
                "The API returned the following status: %d" % r.status_code
                )
```

There we go. This feels more like something that will actually work. I should probably prove that with some tests ...

## Testing the Client ##

Usually, I do most all of my development in a test-driven (or test-first) manner, but when I'm learning a new language, I prefer to get used to the language before I try to get used to its testing mechanisms. At any rate, let's write our first test.

Since we're testing the client, we should probably figure out a way to mock out the actual HTTP requests. Otherwise, we're going to have to be online to run our tests, which is kind of a drag. It turns out, though, that [requests-mock](http://requests-mock.readthedocs.io/en/latest/) is a thing, so let's pull that into our test requirements in `setup.py`:

```python
from setuptools import setup

install_requires=[
    'furl',
    'requests',
    ]

tests_require = [
    'mock',
    'nose',
    'requests-mock',
    ]

setup(
        name = 'maury',
        version = '0.1.0',
        description = 'A experimental client for the Engine Yard API',
        license = 'MIT',
        packages = ['maury'],
        install_requires = install_requires,
        tests_require = tests_require,
        test_suite = "nose.collector",
        zip_safe = False)
```

So far, so good. Now let's try actually writing a test or two in `tests/test_client.py`:

```python
from unittest import TestCase
import requests_mock

from maury.client import Client

class TestResult(TestCase):
    @requests_mock.Mocker()
    def test_get(self, m):
        # The happy path
        m.get('https://api.engineyard.com/sausages', text='gold')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.get('sausages', None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, 'gold')

        # The happy path with params
        m.get('https://api.engineyard.com/sausages?color=gold', text='yep')

        result = c.get('sausages', {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, 'yep')

        # A wild API error appears!
        m.get(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.get('ed209', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.get(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.get('404', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
```

When we run our tests with `python setup.py test`, we get (along with a ton of noise) the following output:

```
test_get (maury.tests.test_client.TestResult) ... ok
```

That sounds like a winner in my book. There are still a few things we should straighten out before we move on, though. First thing being first ... textual responses are fine and all, but we're really more interested in JSON responses.

## JSON ##

The `requests` package is nice enough to automagically convert JSON responses for us, so let's change the tests for that.

```python
from unittest import TestCase
import requests_mock

from maury.client import Client

class TestResult(TestCase):
    @requests_mock.Mocker()
    def test_get(self, m):
        # The happy path
        m.get('https://api.engineyard.com/sausages', text='{"sausages":"gold"}')

        c = Client('https://api.engineyard.com', 'faketoken')
        result = c.get('sausages', None)
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'gold'})

        # The happy path with params
        m.get(
                'https://api.engineyard.com/sausages?color=gold',
                text='{"sausages":"yep"}')

        result = c.get('sausages', {'color' : 'gold'})
        self.assertTrue(result.ok)
        self.assertEqual(result.body, {'sausages' : 'yep'})

        # A wild API error appears!
        m.get(
                'https://api.engineyard.com/ed209',
                status_code = 500,
                text = 'Drop your weapon. You have 20 seconds to comply.')

        result = c.get('ed209', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)

        # PEBCAK
        m.get(
                'https://api.engineyard.com/404',
                status_code = 404,
                text = 'You are now staring into the void. It is staring back.')

        result = c.get('404', None)
        self.assertFalse(result.ok)
        self.assertFalse(result.error == None)
```

If we run the tests right now, we get failures. That's because we changed the test specification, but we haven't changed the code yet. That's awesome, because that's the sort of test-driven thing that allows us to actually change the code intentionally (rather than otherwise). So, let's intentionally change `maury/client.py` so we get JSON in our results instead of raw text:

```python
from furl import furl
import requests
from .result import Result

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url, token):
        """Set the base_url and token for a new Client instance"""

        self.__base_url = base_url
        self.__token = token

    def __construct_request_url(self, path):
        """Construct a URL for an API endpoint.
        
        Given a relative endpoint path, construct a fully-qualified API URL.
        """

        # Get a URL object that we can edit
        u = furl(self.__base_url)

        # Set the path to the endpoint in question
        u.path = path

        # Return the modified URL
        return u.url

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

        if r.ok:
            return Result(r.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % r.status_code
                )
```

Now that we've updated the client, the tests pass again. Sometimes, I do love developering. As you can see, we've also specified that we would like JSON back in our responses via the headers for the request.

If all we ever have to do is handle the `GET` verb, we're done!
