# Up-front Design #

As they all have slightly different requiremnts, it's a little more difficult to do much design for these endpoints as a whole. Still, we can lay out some basic design elements for all of them:

* An endpoint is wholly contained within a maury submodule
* An endpoint contains an Entity class
* An endpoint contains one or more module-level functions
* These module-level functions all take a `Client` instance as their first argument

Let's break that down a bit further.

## Why Submodules? ##

Every formal computer science class that I've taken has emphasized the importance of modular code. The reasoning that's always used is that modular code is code that is easy to re-use. I'm not going to deny that, but I honestly think there's a more important quality to modular code:

A highly modular system contains many clear seams.

What do I mean by "seam?" Much like the seams in your clothing that join two pieces of fabric, a seam in a software system is the methods, references, and so on that allow two pieces of the system to work together. There are a few reasons that seams are handy, but here are the ones that I care about the most, and they're related to each other:

* A seam is a clear, concrete separation of concerns
* A seam gives us a concrete border along which we can mock the code that is not directly under test

### Separation of Concerns ###

In object-oriented design, particularly in terms of [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design), one of the big goals is to limit the number of responsibilities given to a single object. Heck, the Single Responsibility Principle is the "S" in SOLID.

That's fine and good for individual classes, but I like to apply SRP as much as is possible to the module that contains those classes. For example, you'll see in the following chapters that the "accounts" module only does account stuff, the "environments" module only does environment stuff, so on.

### Mocking Along Seams ###

Sometimes, it's incredibly inconvenient to actually run all of the code that's invovled with generating a result in our tests. For example, in our driver implementation, you saw that we used `requests-mock` to fake out the raw HTTP calls that were made.

Generally speaking, there are two big important rules for mocking:

* You cannot mock the code under test
* You can only mock documented interfaces for which you can reasonably replicate behavior

This is usually rolled up neatly as "mock along the seam." In the case of our driver, we don't "own" the upstream API, so that is a natural seam. That being the case, we mocked specific known behaviors of the upstream API.

Generally speaking, it's perfectly fine to mock code along any seam in your system. We'll get deeper into this in the following chapters, and it's a technique that I very much hope carries over into all of your projects if you don't already work this way.

## Entities ##

In both the Data Mapper and the Repository patterns, the actual data object that is returned from the data store is typically referred to as an "entity." In the case of Repository, it's usually something like a Python dictionary, and in the case of Data Mapper, it's typically an object with reader methods for the properties of the object.

Take a look back at the Engine Yard API documentation: more or less every request returns a JSON object that describes one or more instance of the requested resource. Those are entities in the broad sense.

I mentioned that the API client design that I like is somewhat like the Data Mapper pattern overlayed on top of the Repository pattern. That being the case, here's the general design that we'll use for all Entity classes:

* An Entity has a reader for each important property
* An Entity has a general reader that can access any property
* An Entity should be immutable
