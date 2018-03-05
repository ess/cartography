# External Dependencies #

It might seem a bit like putting the cart before the horse, but I'm not very familiar with Python at this point. It makes sense to do a bit of research to find out if it has support for the things that we already know our client needs to do.

Technically, all of the things that we need in order to implement the core driver is provided in the Python standard library. After a bit of comparitive research, though, it seems that the non-standard options provided by the community might well be easier to use (and are often suggested over the standard library).

So, let's take a look at the options.

## HTTP ##

Interestingly, the [documentation](https://docs.python.org/3/library/http.client.html) for Python's standard library `http.client` package directs us to check out a community-provided library instead for a higher-level interface: [requests](http://docs.python-requests.org/en/master/).

After looking at how both of these options are used, I'm *totally* going the easy route by pulling in the `requests` package.

## URL Construction ##

In my experience, we're going to end up building some URLs in this implementation. After a bit of trial and error with Python's built-in mechanism for this, I left with a bad taste in my mouth and went in search for another option.

More googling and a bit of playing around led me to the [furl](https://github.com/gruns/furl) package.

## Testing ##

While researching the above concepts, I started thinking about testing.

We're going to use [nose](http://nose.readthedocs.io/en/latest/) to make writing and running our tests easier. Oh, yeah, we're testing. I'd hate for [Bryan Liles](https://twitter.com/bryanl) to come after me for showing you how to do this stuff without showing you how I [TATFT](https://www.youtube.com/watch?v=iwUR0kOVNs8).

## `setup.py` ##

So, now that we have our external dependencies, let's add them to our `setup.py`:

```python
from setuptools import setup

install_requires=[
    'furl',
    'requests',
    ]

tests_require = [
    'mock',
    'nose',
    ]

setup(
        name = 'maury',
        version = '0.1.0',
        description = 'A experimental client for the Engine Yard API',
        license = 'MIT',
        packages = ['maury'],
        install_requires = install_requires,
        tests_require = tests_require,
        test_suite = "nose.collector",
        zip_safe = False)

```
