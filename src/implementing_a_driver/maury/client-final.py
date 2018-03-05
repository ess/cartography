from furl import furl
import requests
from .result import Result

class Client(object):
    """A base driver that talks to the Engine Yard API"""

    def __init__(self, base_url = 'https://api.engineyard.com', token = None):
        """Instantiate a new Client instance
        
        Keyword arguments:
        base_url -- the base URL of the API (default: 'https://api.engineyard.com')
        token -- the API authentication token (default: None)
        """

        self.__base_url = base_url
        self.__headers = {
                'X-EY-Token' : token,
                'accept' : 'application/vnd.engineyard.com.v3+json',
                'content-type' : 'application/json'
                }

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

    def __process_response(self, response):
        """Process an API response into a Result."""

        if response.ok:
            return Result(response.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % response.status_code
                )

    def __make_request(self, verb, path, params = None, data = None):
        """Send an HTTP request to the server.

        Given an HTTP verb, an endpoint path, a dictionary of parameters,
        and a dictionary of body data, send the request to the API and
        return the result.

        Positional arguments:
        verb -- the HTTP verb to use for the request
        path -- the path of the API endpoint you wish to address

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        data -- a dictionary of POST data (default: None)
        """

        response = requests.request(
                # Uppercase the verb, just in case
                verb.upper(),
                self.__construct_request_url(path),
                params = params,
                json = data,
                headers = self.__headers,
                allow_redirects = True
                )

        return self.__process_response(response)

    def get(self, path, params = None):
        """Perform an HTTP GET on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.

        Positional arguments:
        path -- the path of the API endpoint you wish to GET

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        """

        return self.__make_request('GET', path, params = params)

    def post(self, path, params = None, data = None):
        """Perform an HTTP POST on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        POST data, send the request to the API and return the result.

        Positional arguments:
        path -- the path of the API endpoint you wish to POST

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        data -- a dictionary of POST data (default: None)
        """

        return self.__make_request('POST', path, params = params, data = data)

    def put(self, path, params = None, data = None):
        """Perform an HTTP PUT on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        PUT data, send the request to the API and return the result.

        Positional arguments:
        path -- the path of the API endpoint you wish to PUT

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        data -- a dictionary of PUT data (default: None)
        """

        return self.__make_request('PUT', path, params = params, data = data)

    def patch(self, path, params = None, data = None):
        """Perform an HTTP PATCH on the API.
        
        Given an endpoint path, a dictionary of parameters, and a dictionary of
        PATCH data, send the request to the API and return the result.

        Positional arguments:
        path -- the path of the API endpoint you wish to PATCH

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        data -- a dictionary of PATCH data (default: None)
        """

        return self.__make_request('PATCH', path, params = params, data = data)

    def delete(self, path, params = None):
        """Perform an HTTP DELETE on the API.
        
        Given an endpoint path and a dictionary of parameters, send the request
        to the API and return the result.

        Positional arguments:
        path -- the path of the API endpoint you wish to DELETE

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        """

        return self.__make_request('DELETE', path, params = params)
