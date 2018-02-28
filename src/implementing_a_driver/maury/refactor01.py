    def __process_response(self, response):
        """Process an API response into a Result."""

        if response.ok:
            return Result(response.json(), None)

        return Result(
                None,
                "The API returned the following status: %d" % response.status_code
                )

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

        return self.__process_response(response)

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

        response = requests.post(self.__construct_request_url(path),
                params = params,
                json = data,
                headers = {
                    'X-EY-TOKEN' : self.__token,
                    'accept' : 'application/vnd.engineyard.v3+json',
                    'content-type' : 'application/json',
                    })

        return self.__process_response(response)
