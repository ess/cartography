# GET: the First Verb #

I like to start my implementation with the first, least-destructive HTTP verb in mind: `GET`.

So, let's get started developing our `Client` class. Why am I using a class here? Aside from the general *when in Rome ...* rule (though I'm told that it's almost bad form to do OOP in this OO language, by somebody who's probably trollin'), I have some plans down the line for how this client will be used. Also, our requirements flat out state that we need to keep track of some data: the base URL for the API and an authentication token.

Let's start there! In `maury/client.py`, we'll put the following:

```python
{{#include maury/initial01.py}}
```

There we go. We now have a `Client` class that accepts a base URL and a token. Our work is done!

## Constructing URLs ##

Dangit. Okay. More work it is.

Our requirements say that we need to be able to construct URLs based off of a relative endpoint path. So, let's do that in `maury/client.py`, too:

```python
{{#include maury/initial02.py}}
```

Well, that was easy. That's two requirements down ... let's go for a third.

## Speaking HTTP ##

We need to be able to speak HTTP! Back to `maury/client.py`:

```python
{{#include maury/initial03.py}}
```

It's almost cheating, but simply importing the `requests` package means that we can speak HTTP in this module. Moving on ...

## HTTP GET ##

This might be the most complicated requirement that we've tackled so far, and it's not the lowest-hanging fruit on the list of remaining requirements, but it makes sense to do this next because of reasons.

So, let's implement the first public method in our `Client` class: `get`:


```python
{{#include maury/get01.py}}
```

That's fine and good, and it technically fulfills the `implements HTTP GET` requirement, but there are a few problems with this implementation:

* It won't work: this is an authenticated API, but we're not handling authentication
* It might not work: we haven't specified an API version
* It might not work: we are assuming that the API is always in top notch operational condition and that we are always sending a valid request ... there is no error handling at all

Let's fix those in that order.

## Authentication ##

So, in order to provide our authentication token to the API, we either have to pass it in as part of the query string, or we have to set the `X-EY-TOKEN` header. Between the two of these, the header option is more secure and just plain less messy, so let's do that.

}}
```python
{{#include maury/get02.py}}
```

That's taken care of. Next up is to specify the API version.

## API Version ##

In order to specify the version of the API that we want to use, we have to pass it in as part of the `Accept` header.

```python
{{#include maury/get03.py}}
```

We specified the heck out of that API version, I reckon. One more to go!

## API Error Handling ##

This one might seem a bit weird if you're actually familiar with Python, but since I'm not particularly, I'm going to do the thing that makes the most sense to me, heavily influenced by other languages that I know better.

You see, the thing here is that I don't actually know much about how to handle exceptions in Python, and I actually don't like using exceptions for error handling. Some of my favorite languages use some form of multiple return for error handling. While I could do that with a `list` or a `tuple`, there's a technique that I prefer: let's make a `Result` class in `maury/result.py`:

```python
{{#include maury/result.py}}
```

Now that we have a way to express both positive and negative results, let's tie it in and use it in our `Client`:

```python
{{#include maury/get04.py}}
```

There we go. This feels more like something that will actually work. I should probably prove that with some tests ...

## Testing the Client ##

Usually, I do most all of my development in a test-driven (or test-first) manner, but when I'm learning a new language, I prefer to get used to the language before I try to get used to its testing mechanisms. At any rate, let's write our first test.

Since we're testing the client, we should probably figure out a way to mock out the actual HTTP requests. Otherwise, we're going to have to be online to run our tests, which is kind of a drag. It turns out, though, that [requests-mock](http://requests-mock.readthedocs.io/en/latest/) is a thing, so let's pull that into our test requirements in `setup.py`:

```python
{{#include maury/setup01.py}}
```

So far, so good. Now let's try actually writing a test or two in `tests/test_client.py`:

```python
{{#include maury/test_client01.py}}
```

When we run our tests with `python setup.py test`, we get (along with a ton of noise) the following output:

```
test_get (maury.tests.test_client.TestResult) ... ok
```

That sounds like a winner in my book. There are still a few things we should straighten out before we move on, though. First thing being first ... textual responses are fine and all, but we're really more interested in JSON responses.

## JSON ##

The `requests` package is nice enough to automagically convert JSON responses for us, so let's change the tests for that.

```python
{{#include maury/test_client02.py}}
```

If we run the tests right now, we get failures. That's because we changed the test specification, but we haven't changed the code yet. That's awesome, because that's the sort of test-driven thing that allows us to actually change the code intentionally (rather than otherwise). So, let's intentionally change `maury/client.py` so we get JSON in our results instead of raw text:

```python
{{#include maury/get05.py}}
```

Now that we've updated the client, the tests pass again. Sometimes, I do love developering. As you can see, we've also specified that we would like JSON back in our responses via the headers for the request.

There's one last bit of business to take care of before we consider this iteration complete.

## Revisiting Result ##

The `Result` class looks good. It gives us a clean way to communicate back to the code that's using our `Client`. But does it? We should illustrate that with a test in `tests/test_result.py`:

```python
{{#include maury/test_result.py}}
```

That does it. If all our client ever has to do is provide the ability to make `GET` requests against the API, we're done!
