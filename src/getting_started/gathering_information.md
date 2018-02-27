# Gathering Information #

In the case of the Engine Yard API, there's actually quite a lot of information that we can get from the [API overview](https://developer.engineyard.com):

* It's an authenticated HTTP API
* The authentication token can be passed in either as part of the query or as the `X-EY-TOKEN` request header
* From this page, we know that the `GET`, `POST`, `PUT`, and `PATCH` HTTP verbs are used
* We know that the API can both accept and serve the `application/json` MIME type
* From the sidebar, we can see that there are a good number of endpoints off of the API root

Taking a look around at some of those endpoints, we learn even more about this specific API:

* The API is versioned
* The desired API version is specified as part of the `Accept` request header: `application/vnd.engineyard.v3+json`
* The `DELETE` HTTP verb is also used in this API
