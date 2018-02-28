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
