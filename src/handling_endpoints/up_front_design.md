# Up-front Design #

As they all have slightly different requiremnts, it's a little more difficult to do much design for these endpoints as a whole. Still, we can lay out some basic design elements for all of them:

* An endpoint is wholly contained within a maury submodule
* An endpoint contains an Entity class
* An endpoint contains one or more module-level functions
* These module-level functions all take a `Client` instance as their first argument

Let's break that down a bit further.

## Why Submodules? ##

## Entities ##


