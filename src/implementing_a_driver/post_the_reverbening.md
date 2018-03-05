# POST: the Reverbening #

Of course, our requirements state that we have to also be able to make `POST` requests to the API. So, we have more work cut out for us. Luckily, the handling of any given verb is quite a lot like the handling of any other given verb.

## A Note From Our Sponsors ##

Yeah, not really. More than anything, I wanted to take this opportunity to let you know that from this point on, listing the entirety of the referenced files would become unwieldy rather quickly.

So, from now on, I'll just show the changes in the code examples instead of the entire file, where possible.

## Test-Driven ##

Now that we're a little more familiar with the language and its unittest framework, let's change gears a bit. We're going to start our `POST` feature with a new test in `maury/tests/test_client.py`:

```python
{{#include maury/test_client-final.py:46:83}}
```

As you can see, our `post` test is almost identical to our `get` test. That's because, as mentioned above, all of the verbs are handled in more or less the same way. The big difference here is that `post` involves not just a path and a params dict, but also a dict of data to be `POST`ed to the endpoint.

After running our tests, we see that our `test_post` test yields an error. That's because we don't have a `post` method in our client yet. Let's do that.

## First Draft Implementation ##

Since they test the same (aside from the extra argument), it stands to reason that `get` and `post` should have rather similar implementations. Let's do a quick copypasta in `maury/client.py` and see how that works out:

```python
{{#include maury/post01.py}}
```

Running our tests now yields a success:

```
test_post (maury.tests.test_client.TestResult) ... ok
```

So, one could argue that we're done at this point, but there's something that's bugging me a bit about this implementation. Take a look at the `get` and `post` methods. Notice how similar they are? We should probably take this opportunity to go ahead and refactor those similarities away.

## Refactoring? ##

For those not used to the term or the practice, refactoring is basically the act of rearranging the code within a program to increase the simplicity of the system without altering its behavior. That's not really the proper definition of the term, but that is the way that I think about it.

There are a several interpretations one could use for "simplicity" in this context. I think about two things:

* How easy is it to figure out how the module works?
* How *smelly* is the code?

Our client module is fairly small, and it's not very difficult to figure out how it works for the moment. However, it ***is*** slightly smelly due to the high degree of code duplication between the `get` and `post` methods. In addition to this, each of those high-duplication methods also have variant execution paths depending on the API response.

We can't totally remove the duplicated code and those variant conditional execution paths, but we ***can*** minimize those smells by method extraction.

Before we start, let's set some ground rules that we will use every time we refactor anything going forward:

* We ***MAY*** change the module that we're refactoring
* We ***MAY*** create new methods within the module
* We ***MAY*** create new modules and hand work off to them
* We ***MAY NOT*** alter our tests (otherwise, we're redesinging, not refactoring)
* We ***MUST*** have a passing test suite after every change (otherwise, we have broken our module)

## Refactoring: Response Processor ##

So, one of the things that makes these two methods so similar, aside from all verbs being very similar in the first place, is that they both interpret the API response identically. That being the case, we can construct a common method to use for response processing in `maury/client.py`:

```python
{{#include maury/refactor01.py}}
```

That's a little better, and thanks to our tests, we can see that the behavior has not changed. Yay TDD! Still, I see at least one more thing that I don't like: those repeated headers seem like a perfect aspect to reconsider.

## Refactoring: Headers ##

Now, there are a lot of ways that we could switch up the request headers dictionary. I usually go for a private method for things like this, but I'm also not familiar enough with Python to know how much of an impact on resource usage and performance constantly generating new dicts will have. That being the case, let's jump into `maury/client.py` and see if we can find another way:

```python
{{#include maury/refactor02.py}}
```

What we did there was to store the headers dictionary directly in the client object as `__headers`. Also, since we don't use the token for anything else, we are no longer storing the token at all. Also, the tests still pass, so it looks like we're still good.

## Refactoring: What's Next? ##

Can we go further? Sure, we can, but at this point, we probably shouldn't.

So far, all verb implementations have involved making an API request, then processing the API response. We have implemented less than half of the verbs that we have to implement, though.

That being the case, let's follow the advice that I'd imagine Sandy Metz would give right now: let's just keep working on the requirements until we're ***sure*** that we can safely refactor further.
