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
