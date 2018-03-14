# Entity #

This is the first entity that we're defining, so it's going to be a bit more work than the entities for pretty much all other endpoints. Let's review the general requirements for an Entity:

* It must have a general reader for any property
* It must have a specific reader for all important properties
* It should be immutable

Why would we want the Entity to be immutable (or as close as we can get to it in Python)? In the end, I can bring up several arguments both for and against the notion of immutable data. The reality here is that after working for a long time with both sorts of systems, I've had a much better experience with those that treat data as data.

I don't have a lot of incredibly strong opinions about developering in general, but the idea that data should be data and nothing more is definitely a member of that club.

## General Reader ##

So, we want to be able to read any given property (by key) from the entity. Let's start with a test and work backwards from there. Since we're effectively just fetching a value from a dictionary, let's call the method `fetch` and add our test to `maury/tests/test_accounts.py`:

```python
{{#include entity/test.py:1:17}}
```

That seems to cover the basic rules around `fetch`: if the key is in the Entity's data dictionary, we return the value for that key. Otherwise, we return `None`. Granted, if we run that test, we get an error about the class not existing. Let's fix that in `maury/accounts.py`:

```python
{{#include entity/entity.py:1:4}}
```

That's enough to run our tests and ... get a different error. Such is the nature of the test-driven development beast. Now it's complaining that we can't actually instantiate an Entity the way that we're trying to, so let's fix that:

```python
{{#include entity/entity.py:6:16}}
```

We're getting closer. Now we get yet another error, and it's because we haven't a `fetch` method for our Entity objects. Back to `maury/accounts.py`:

```python
{{#include entity/entity.py:6:16}}

{{#include entity/entity.py:18:25}}
```

Now we're getting somewhere. We're no longer getting Python errors when we run our accounts test ... now we're getting an actual test failure:

```
FAIL: test_entity_fetch (maury.tests.test_accounts.TestAccounts)
```

Looking a bit further, we see that our primary assertion is not being provided by our `fetch` implementation. That is, right now, `fetch` literally doesn't return anything (it returns the default Python return, `None`). So, let's make it return the expected information:

```python
{{#include entity/entity.py:18:23}}

{{#include entity/entity.py:26}}
```

Alright, our first assertion passes ... which leads us to another Python error in our tests:

```
KeyError: unknown key
```

That indicates that our second scenario is failing (though we could arguably be testing that in a way to produce a failure rather than an error). So, what we want is for `fetch` to return the actual requested data if the key is known, but to return a default `None` value if the key is not known. Since it's guaranteed that an Entity's internal `__data` is a `dict`, we can use a handy method for that:

```python
{{#include entity/entity.py:18:23}}

{{#include entity/entity.py:27}}
```

Our tests are now passing, and that's awesome. We've implemented a general reader for any data property of an account entity.

## Specific Readers ##

We also require that the Entity have a specific reader for all "important" data properties to make things easier for the end-users of our client. We're nice folks like that. So, let's head back over to the [Accounts docs](https://developer.engineyard.com/accounts) and figure out what some of the important properties are.

At least for now, I've narrowed it down to basically the following:

* id -- the identifier used on the API to reference the account
* name -- the name used on the API to reference the account
* emergency_contact -- the emergency contact for the account

### Account ID ###

Let's start by adding a test to `maury/tests/test_accounts.py`:

```python
{{#include entity/test.py:19:31}}
```

This test is actually quite a lot like our `fetch` test, as do the initial results. That being the case, let's go ahead and implement the `id` method by using the `fetch` method:

```python
{{#include entity/entity.py:29:33}}
```

Boom. Our tests pass, and we can move on to the next reader.

### Name and Emergency Contact ###

The other two specific readers are just riffs on the `id` reader. Let's go ahead and add the tests for those to `maury/tests/test_accounts.py`:

```python
{{#include entity/test.py:33:59}}
```

We already know that these tests fail, and we already know why ... there's not an implementation for these properties. Let's go ahead and add them to `maury/accounts.py`:

```python
{{#include entity/entity.py:35:45}}
```

Boom. Our tests pass, and all of our (currently required) specific readers are implemented.

## Immutability ##

The last requirement that we have is that entities should be immutable. If I understand everything properly, this is unfortunately not technically possible for third-party types, like our `Entity` class.

To that end, we're using Python's social conventions to get as close as we can here (without dropping down to C to implement our data structure). That is, an Entity's data is stored in its `__data` member, and the social convention in Python is to not directly access methods and members that begin with `__`.

I'd personally prefer a stronger guarantee here. That said, this tradeoff also happens in just about all of the existing `maury` implementations (the notable exception being `maury-rust`).

So, while it's technically possible for somebody using our client to modify the makeup of a given account Entity, it would be bad form for them to do so.
