# Howdy! #

Have you ever wanted to create your very own client for a REST API? That's what this book is all about.

## What's A REST API? ##

There's quite a pair of acronyms right there. Let's break it down a bit:

* ***REST***, or [REpresentational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer), basically describes a specific way that one can use web requests to get information from the remote system and subsequently do things with that data, still on the remote system.
* An ***API***, or [Application Programming Interface](https://en.wikipedia.org/wiki/Application_programming_interface) is a collection of functions, procedures, or system calls that one uses to make their program work with a piece of software that is not itself.

Bringing it all together, a ***REST API*** is a remote system that allows us to use that system for our programs as if it was a part of our program.

The best layman analogy that I have for this is my dog, Jake:

* When I look at Jake and say "sit," he ignores me, but in a perfect world, he would sit.
* When I look at Jake and say "good boy," he wags his tail.
* When I look at Jake and say "potty," he runs for the door.

The API for the K9-Jake Supercomputer is "sit," "good boy," and "potty." If he were hooked up to a web server (please, don't form a mental image of this, nothing good can come from it), there would be an equivalent REST API.

A client is a package that knows specifically how to talk to the REST API for which it is written, generally making it easier to interact with that API in your own programs.

## Just Who Do I Think I Am? ##

Hi there, I'm Dennis, and I'm a Professional Services Engineer at [Engine Yard](https://www.engineyard.com). Really, that's just a fancy way to say that I do the "whatever it takes" on behalf of customers that have very custom needs.

I've been creating software and API consumer libraries for a pretty long time, and the latter of those ideas is something that I inexplicably enjoy quite a lot.

When I'm not doing that sort of thing, I can sometimes be found drawing, trying to get better at basement lutherie, making music on computerboxes, or convincing my dog that it's totally okay if he wants to leave me a few inches on the bed.

## Just Who Do I Think You Are? ##

Hi there, you're you. As I see it, there are a few possibilities as to who you are:

* You might be a friend or colleague that I've asked to read over this book to help me figure out how to most effectively communicate the ideas that I'm presenting
* You might be a relatively new software developer that needs to figure out how to consume an API for which there is not an existing client
* You might be a seasoned software developer that is looking for a different approach to API client design
* You might even be a person that hasn't touched a computer before, but wants to learn about the way things like the Twitter and Facebook mobile apps communicate with their respective services

Regardless of who you are, I very much hope that you enjoy the ride.

## Why "Cartography?" ##

Every REST API that I've used, regardless of how well documented they may be, has required me to do a bit of journeying and mapping along the way to figure out how things really work. As a reflection of this, the API provider will often publish clients for the popular languages of the day, but that isn't always the case.

For example, the [Engine Yard API](https://developer.engineyard.com) is relatively well-documented, and Engine Yard does provide [a Ruby client](https://github.com/engineyard/core-client-rb), but what if I want to consume this API from a Python program?

That is the example that we'll use for the purposes of this illustration: implementing a Python client for the Engine Yard API. That said, the techniques used here should be fairly easily adapated to nearly any language or API (web based or otherwise).

## About This Book ##

Effectively, this book is a quasi-real-time illustration of the designs and processes that I use for charting the seas of web APIs. When a new term or acronym appears, I'll do my best to break it down for folks that might not be familiar, but there's a decent chance that I'll gloss over one or two along the way due to their ubiquity in the field.

Also, there will be quite a lot of Python code in this book. When you've finished, if you've diligiently typed out all of the examples into the correct files, you'll actually have a working client for the API that I'm mapping. If you'd like to forego that process, you can find the finished client [on Github](https://github.com/ess/maury.py), but I promise that you'll learn more the other way.

In the beginning those code examples will be entire files, but as we progress and those files become large, snarling behemoths, I'll start showing only the parts that change. Don't worry, though, I'll let you know exactly where that happens.

Every now and then, I'll drop in a list of questions that won't have answers. You don't strictly have to do these exercises, but I'd strongly urge you to do so, because learning is learning, and learning is awesome.

## Acknowledgements ##

These people greatly helped me along the way by reading the various iterations to make content suggestions, point out things that I've forgotten, increase readability and comprehensibility, or even just finding typos.

These are good people. You should find them and listen to the things that they have to say as well.

* [Adam Delong](https://github.com/delongshot)
* [Carlos Cano](https://github.com/superflit)
* [Daniel Valfre](https://github.com/dvalfre)
* [Matt Jones](https://github.com/halposhaven)
* [Radamanthus Batnag](https://github.com/radamanthus)

## A Few Caveats ##

As seems to be the case with all books like this one, there are a few things that should probably be stated up front:

* As mentioned above, I'm currently employed by Engine Yard. While one might argue that I've chosen the Engine Yard API as the example for this book to be a sign of bias, the reality is that I've chosen it because it's a fairly complicated (to the point of being difficult) API to consume, and there are some hidden gems in it that can help to illustrate how one might handle situations in which they're stuck.
* This very much is not the only way that one could develop an API client. This is, however, the method that I prefer, so I'm rolling with it.
* Python is being used as the implementation language in this book, but this is just an example of a language that is not officially supported by the API provider. As it were, there are partial implementations of the client that is being developed in this book in the following languages: Go, Javascript, ooc, Ruby, and Rust
* I don't actually know Python, so this will be a learning experience for me as well. I'm using Python 3.6.4 locally to develop this client as we go, but it's important to note that this should probably not be considered an example of idiomatic Python code, let alone high-quality Python code. I honestly don't know Python well enough to even be able to make that previous statement.
