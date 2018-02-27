# Odds and Ends #

Keep in mind, I said that it's *technically* complete, in as much as it does everything that we need for it to do. That doesn't necessarily mean that we're done, though.

How usable is the `maury` package right now? How many layers of documentation and submodules does one have to dig through to find out how to create a `Client`?

## An Entrypoint ##

While it's not strictly necessary, I like to provide an easy entrypoint at the top-level of the package for things that get used a lot. That way, a developer using my library can just import the top level package, ask it for a client, and get rolling.

First thing first, let's add a test for the function that we want to create in `maury/tests/test_new_client.py`:

```python
from unittest import TestCase

import maury

class TestNewClient(TestCase):
    def test_is_client(self):
        s = maury.new_client('https://example.com', 'token12345')
        self.assertIsInstance(s, maury.Client)
```

That's a pretty simple test (almost too simple, really), but it will do for our purposes right now. What's more, it fails if we try to run our tests right now, so we're definitely on the right track! Let's go ahead and implement this function in `maury/__init__.py`:

```python
from .client import Client

def new_client(base_url, token):
    return Client(base_url, token)
```

## Conclusion ##

Now we have a *somewhat friendly* and complete driver for the API that we're mapping. That's it for Phase 1, and now we're ready to move on to Phase 2.

Feel free to take a break. Phase 2 is, if you can imagine it, a lot more reliant on code snippets than Phase 1 is, and it's also a rather tedious and repetitive affair.

Also, just to be clear, you don't ***have*** to go any further than you already have. If you simply want to provide a lowish-level client that knows how to talk to the API that you're mapping so others can have a handy building block on which to build their API interactions, you're done. I like to go a little further than that, though, so I'll go ahead and trudge forward.
