# Howdy! #

Have you ever wanted to create your very own client for a REST API? That's what this book is all about.

Why "cartography?" Well, a lot of the REST APIs out there, regardless of how well documented they may be, require for us to do a bit of journeying and mapping along the way to figure out how things really work. A lot of the time, the API provider will go ahead and publish clients for the popular languages of the day because of the above conundrum, but that isn't always the case.

For example, the [Engine Yard API](https://developer.engineyard.com) is relatively well-documented, and Engine Yard does provide [a Ruby client](https://github.com/engineyard/core-client-rb), but what if I want to consume this API from a Python program?

That is the example that we'll use for the purposes of this illustration: implementing a Python client for the Engine Yard API. That said, the techniques used here should be fairly easily adapated to most any language or API.

## A Few Caveats ##

As seems to be the case with all books like this one, there are a few things that should probably be stated up front:

* I'm currently employed by [Engine Yard](https://www.engineyard.com) as a Professional Services Engineer, which is really just a fancy way to say that I do the "whatever it takes" on behalf of customers that need very custom setups. The use of the Engine Yard API as the example for this book is mostly because it is a somehat complicated (to the point of being difficult) API to consume.
* This very much is not the only way that one could develop an API client. This is, however, the method that I prefer, so I'm rolling with it.
* Python is being used as the implementation language in this book, but this is just an example of a language that is not officially supported by the API provider. As it were, there are partial implementations of the client that is being developed in this book in the following languages: Go, Javascript, ooc, Ruby, Rust
* I don't actually know Python, so this will be a learning experience for me as well. I'm using Python 3.6.4 locally to develop this client as we go, but it's important to note that this should probably not be considered an example of idiomatic Python code, let alone high-quality Python code. I honestly don't know Python well enough to even be able to make that previous statement.
