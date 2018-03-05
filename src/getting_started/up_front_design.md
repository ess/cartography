# Up-front Design #

Now that we have some information about the API that we're mapping, we can start designing our client. Here's what we know:

* We need to be able to handle HTTP interactions with a JSON-centric REST API
* That API is authenticated
* That API is versioned
* That API uses an uncommon version specification strategy
* We need to be able to handle multiple endpoints on that API

We'll break those down a bit further in a few minues, but before we do that, we should think a bit about the overall design of our client.

## Our Design ##

There are a few schools of thought as to what an API client should look like. At the extremes of that group are basically "a library full of functions" and "a web ORM."

I prefer something that's a bit between the two.

For nearly every API client that I've written, I've gone with a design that looks a lot like the Data Mapper pattern overlaid on top of a Repository. I'm not incredibly familiar with libraries that work this way outside of the Ruby community. From that community, though, the best examples are probably [Ruby Object Mapper](http://rom-rb.org/) and [Hanami Model](https://github.com/hanami/model).

What we're going to do is to break this API client project into two main phases:

1. First, we're going to create a HTTP driver that interfaces with the REST API. This driver is basically our doorway to all communication with the upstream API. It takes care of authentication, request and response handling, and is really the core of the whole deal.
2. The second phase is the modeling of the upstream API endpoints and the data structures specific to them.

## Name ##

Before we move forward, the hardest part of the whole project needs to be done: we need to name the project. In keeping with the naming for my other EY API client implementations, I've called this project [maury](https://en.wikipedia.org/wiki/Maurice_W._Graham), but you can call it anything that you'd like.

With that, let's be a bit proactive and determine the external dependencies that we want to use for the project.


