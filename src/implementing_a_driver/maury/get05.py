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

    def get(self, path, params = None):
        """Perform an HTTP GET on the API.

        Given an endpoint path and a dictionary of parameters, send the request
        to the aPI and return the result.

        Positional arguments:
        path -- the path of the API endpoint to GET

        Keyword arguments:
        params -- a dictionary of query params (default: None)
        """

        response = requests.get(self.__construct_request_url(path),
                params = params,
                headers = {
                    'X-EY-TOKEN' : self.__token,
                    'accept' : 'application/vnd.engineyard.v3+json',
                    'content-type' : 'application/json',
                    })

        if response.ok:
            return Result(response.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % response.status_code
                )

