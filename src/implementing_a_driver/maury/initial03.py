from furl import furl
import requests

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
