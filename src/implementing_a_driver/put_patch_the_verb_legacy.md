# PUT/PATCH: the Verb Legacy

While it's not strictly the case, `PUT` and `PATCH` are fairly often used interchangeably on REST APIs. In the previous section, we implemented the `POST` verb, which is typically used for creating a brand new entity on the remote service. In contrast, `PUT` and `PATCH` are most typically used to update an entity that already exists. Considering that they are often used synonymously, we're going to go ahead and implement these at the same time.

## Tests ##

Another fortunate bit is that `put` and `patch` have the same signature as `post`. That being the case, let's go ahead and copypasta the `post` test in `maury/tests/test_client.py` and modify it for our new methods:

```python
{{#include maury/test_client-final.py:85:161}}
```

As expected, these tests fail, as we don't yet have either the `put` or `patch` mehods in our client.

## Implementing the Methods ##

So, let's crack open `maury/client.py` again, copypasta the `post` method, and modify it to fit our new methods:

```python
{{#include maury/client.py:89:129}}
```

With that, our tests pass, and we've now implemented 80% of the HTTP verbs that we need to meet our requirements. That means it's time to take another look and decide if we should refactor further.

## Refactoring: Request Handler ##

It might seem obvious that since we've already made a common method to handle the processing of an API response that it would also make sense to break out a method that performs the requests in question.

That is a fine observation, and it is indeed what I would usually do myself. I'm not going to do so here, but let's explore it a bit.

In languages with which I have a higher degree of familiarity, I do HTTP requests the "hard" way. That is, so far, we've been doing things the easy way with methods like `request.get()`. What I'll usually do is to wrap the HTTP module's generic method is to send a request to the server, specifying the verb along the way. Then, my verb-related methods just dispatch to that wrapper.

In Python, it would look something like this (docstrings shortened for brevity):

```python
{{#include maury/refactor03.py:1:24}}
```

Granted, if we run our test suite right now, we get just a ton of errors, because we changed the verbs. The `requests` package, contrary to my initial thoughts, will allow us to do things the hard way pretty easily. So, let's fill in that `__make_request` method:

```python
{{#include maury/refactor03.py:26:39}}
```

Okay, that's actually not so bad. The only reason that it leaves a bad taste in my mouth at all is that finding `requests.request()` was a bit difficult. It ***is*** mentioned in the docs (under the Advanced Usage section), but that's not how I found it. I actually ended up digging through the [source](https://github.com/requests/requests/blob/master/requests/api.py) until I figured out how `requests.get()` works, then working backwards.

As it were, that's also where I got the `allow_redirects` argument. All of the verb-related methods in the `requests` package set this argument to `True` by default before dispatching to the `request()` method, so it seems a good idea for us to do so as well. Another fun tidbit: our driver's verb implementations now work almost identically to the way that the verbs in the `requests` package do.

I rather like this design. Our public verb methods don't do any heavy lifting. Instead, they dispatch to private (not really, but by Python social convention) methods that do *all* of the heavy lifting.
