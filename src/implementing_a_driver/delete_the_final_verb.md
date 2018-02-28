# DELETE: the Final Verb #

Our driver is very nearly complete. We only have one verb left to go, so let's get to it!

## Test ##

As it would happen, `delete` has the same signature and expectations as `get`, so let's go ahead and copypasta `test_get` and modify it to `test_delete` in `maury/tests/test_client.py`:

```python
{{#include maury/test_client-final.py:163:200}}
```

Okay, we have a failing test now, so we're going to do the obvious.

## Implementing DELETE ##

Since the signature is the same as `get`, we're going to copypasta the `get` method definition and modify it to fit our new `delete` method in `maury/client.py`:

```python
{{#include maury/client.py:131:148}}
```

There we have it. Now that all of the defined requirements are met and all of our tests pass, our client driver is technically complete.
