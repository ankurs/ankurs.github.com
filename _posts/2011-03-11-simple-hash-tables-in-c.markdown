---
comments: true
date: 2011-03-11 19:37:46
layout: post
slug: simple-hash-tables-in-c
title: Simple hash tables in c
wordpress_id: 764
tags:
- C
- hast
- Simple
- table
---

I was working on a code where i had to lookup a structure based on the file descriptor (socket) again and again in a code, i was using a linked list initially but as the nodes grew i knew i should use a hash table, so i wrote a simple hash table implementation which did the work.

its a _just works_ implementation there are a lot of thing which can be added like a [perfect hash function](http://en.wikipedia.org/wiki/Perfect_hash_function) but as long as hash table is not the bottle neck this should work, code can be found on [github](http://github.com/ankurs/Hash-Table/)

file [hashtable.h](https://github.com/ankurs/Hash-Table/raw/master/hashtable.h) contains the definition
<script src="https://gist.github.com/865909.js?file=hashtable.h"> </script>

file [hashtable.c](https://github.com/ankurs/Hash-Table/raw/master/hashtable.c) contains the implementaion

file [Makefile](https://github.com/ankurs/Hash-Table/raw/master/Makefile) is the makefile

file [main.c](https://github.com/ankurs/Hash-Table/raw/master/main.c) contains the sample

file [debug.h](https://github.com/ankurs/Hash-Table/raw/master/debug.h) contains some debugging options


