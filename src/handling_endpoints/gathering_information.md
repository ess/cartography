# Gathering Information #

When we did the initial documentation investigation to develop our driver, we gave just a very quick glance at the documentation for the individual endpoints. Now we're going to dig in a bit further to find traits that are common to all of those endpoints.

Looking only at the lists at the beginning of each endpoint page, we can get the following information:

* With few exceptions, all endpoints have a way to get a list of entities
* With few exceptions, all endpoints have a way to get a single entity
* Only a few of the endpoints have meaningful write operations
* A few endpoints have RPC-like operations that can be performed
* Most endpoints can be used as a sub-endpoint of another endpoint (ie "get all accounts for a user")

Looking a bit further on each of these pages, we can glean even more information about those above concepts:

* When listing entities from an endpoint, the returned object is a root node with a list, and the name of that node is the entity type of items in the list
* When getting a single entity from an endpoint, the returned object is a root node with an embedded object, and the name of that node is the entity type of that embedded object
* When querying for either multiple entities or a single entity, most endpoints support passing in a list of query params to filter the result
