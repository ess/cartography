# Implementing A Driver #

We're now entering Phase 1 of the project: implementing the core HTTP driver for the client.

To that end, let's take the information that we gathered in the previous chapter and generate the requirements for the driver.

## Driver Requirements ##

We already have a name for the project. Now that the hardest part of any project is over with, we should identify the base requirements for our core client driver:

* It must speak HTTP
* It must accept an authentication token
* For the sake of flexibility, it should also accept the base URL for the API
* It must be able to use the HTTP verbs in question: `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`
* It must be able to set the `X-EY-TOKEN`, `Content-Type`, and `Accept` headers
* For convenience, it should treat all requests as relative, so it must be able to build URLs for each request

That doesn't really sound like a lot, but the driver that we implement through the rest of this chapter is all we *really* need to work with the API. Don't worry, we're not stopping there at all. We have to crawl before we can walk, though.

So, let's get started crawling.
