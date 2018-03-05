    def __make_request(self, verb, path, params = None, data = None):
        """Send an HTTP request to the server."""

        # send the request to the server, return the processed response

    def get(self, path, params = None):
        """Perform an HTTP GET on the API."""

        return self.__make_request('GET', path, params = params)

    def post(self, path, params = None, data = None):
        """Perform an HTTP POST on the API."""

        return self.__make_request('POST', path, params = params, data = data)

    def put(self, path, params = None, data = None):
        """Perform an HTTP PUT on the API."""

        return self.__make_request('PUT', path, params = params, data = data)

    def patch(self, path, params = None, data = None):
        """Perform an HTTP PATCH on the API."""

        return self.__make_request('PATCH', path, params = params, data = data)

    def __make_request(self, verb, path, params = None, data = None):
        """Send an HTTP request to the server."""

        response = requests.request(
                # Uppercase the verb, just in case
                verb.upper(),
                self._construct_request_url(path),
                params = params,
                json = data,
                headers = self.__headers,
                allow_redirects = True
                )

        return self.__process_response(response)
