---
comments: true
date: 2011-03-13 03:02:24
layout: post
slug: a-small-epoll-wrapper
title: small epoll wrapper
wordpress_id: 773
tags:
- callback
- epoll
- function
- Simple
- small
- wrapper
---

I remember my first encounter with epoll some time back trying to get a simple server working, implementing a proxy and then a few days back i saw one of my friend trying to get started with epoll, which made me think it will be good to have a simple wrapper around epoll which will allow me to get started with the application and not worry about epoll specifics and at the same time providing enough control, so i wrote a small wrapper with callbacks, which has been quite helpful for my epoll usage, here is the interface [poll.h](https://github.com/ankurs/Poll-Event/blob/master/poll.h)

<script src="https://gist.github.com/867567.js?file=poll.h"> </script>

code and a sample can be found on [github](https://github.com/ankurs/Poll-Event)

PS - just checkout [libevent](http://www.monkey.org/~provos/libevent/) which is an awesome battle tested event notification library, and a quick [getting started](http://www.wangafu.net/~nickm/libevent-book/)
