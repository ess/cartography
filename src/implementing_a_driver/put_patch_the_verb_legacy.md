# PUT/PATCH: the Verb Legacy

While it's not strictly the case, `PUT` and `PATCH` are fairly often used interchangeably on REST APIs. Considering this, we're going to go ahead and implement these at the same time.

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

## Refactoring: Reqeust Handler ##

It might seem obvious that since we've already made a common method to handle the processing of an API response that it would also make sense to break out a method that performs the requests in question.

That is a fine observation, and it is indeed what I would usually do myself. The problem here is that my lack of Python knowledge is preventing me from coming up with the best way to do so. So, I'm going to keep on going the way that we have been and leave this refactoring to you, if you choose to do it.
