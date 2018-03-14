class Entity(object):
    """A data structure model for an Account"""

    pass

class Entity(object):
    """A data structure model for an Account"""

    def __init__(self, data = {}):
        """Instantiate an Entity with some data"""

        self.__data = data

        # Ensure that __data is a dict
        if type(self.__data) is not dict:
            self.__data = {}

    def fetch(self, key):
        """Get a data property from the Entity
        
        Positional Arguments:
        key -- the name of the data property we wish to access
        """

        pass
        return self.__data[key]
        return self.__data.get(key, None)

    @property
    def id(self):
        """Get the account's ID"""

        return self.fetch('id')

    @property
    def name(self):
        """Get the account's name"""

        return self.fetch('name')

    @property
    def emergency_contact(self):
        """Get the account's emergency contact"""

        return self.fetch('emergency_contact')


