# Initial Specification #

Now that we have done a bit of investigation and know a few things about the API with which we're working, we should put the results of that investigation to use.

First off, we need to name the project. In keeping with the naming for my other EY API client implementations, I've called this project [maury](https://en.wikipedia.org/wiki/Maurice_W._Graham), but you can call it anything that you'd like.

## Client Requirements ##

Now that the hardest part of any project is over with, we should identify the base requirements for our core client driver:

* It must speak HTTP
* It must accept an authentication token
* For the sake of flexibility, it should also accept the base URL for the API
* It must be able to use the HTTP verbs in question
* It must be able to set the `X-EY-TOKEN`, `Content-Type`, and `Accept` headers
* For convenience, it should treat all requests as relative, so it must be able to build URLs for each request

That doesn't really sound like a lot, but the driver that we implement through the rest of this chapter is all we *really* need to work with the API. Don't worry, we're not stopping there at all. We have to crawl before we can walk, though.

## Library Support ##

Technically, all of the things that we need in order to implement the core client driver is provided in the Python standard library. That being the case, after a quick google around, it looks like the community has decided on a better alternative to the HTTP client provided by std: [requests](http://docs.python-requests.org/en/master/).

Additionally, after a bit of quick playing around with the URL parser provided by the standard library, I learned that I can't actually use it to build a URL, which is at least a little important, given that we need to build a URL for every request that the driver handles. More googling led me to the [furl](https://github.com/gruns/furl) package.

Finally, we're going to use [nose](http://nose.readthedocs.io/en/latest/) to make writing and running our tests easier. Oh, yeah, we're testing. I'd hate for [Bryan Liles](https://twitter.com/bryanl) to come after me for showing you how to do this stuff without showing you how I TAFT.

So, now that we have some requirements, let's add them to our `setup.py`:

```python
from setuptools import setup

install_requires=[
    'furl',
    'requests',
    ]

tests_require = [
    'mock',
    'nose',
    'requests-mock',
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
