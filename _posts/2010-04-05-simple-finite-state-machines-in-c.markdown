---
comments: true
date: 2010-04-05 03:12:15
layout: post
slug: simple-finite-state-machines-in-c
title: Simple Finite State Machines in C
wordpress_id: 617
tags:
- C
- finite
- fsm
- machine
- state
---

I was having discussion about State Machines with one of my friend, regarding pro's and con's of implementing programs as Sate Machines, it was then that i realised there is no simple way to implement programs as Finite State Machines, so here is a very basic implementation of FSM in C [github repo](https://github.com/ankurs/FSM)

file: [fsm.h](http://gist.github.com/raw/355708/8046352e1209396bc7485dfa8e7ab9236d685e89/fsm.h) contains the function definition for our FSM
<script src="https://gist.github.com/355708.js?file=fsm.h"> </script>

file: [fsm.c](http://gist.github.com/raw/355708/4a1b7b3d51b5f470a6c5e4344fb69e5e1ebbebc4/fsm.c) contains the function implementation for our FSM
<script src="https://gist.github.com/355708.js?file=fsm.c"> </script>

file: [main.c](http://gist.github.com/raw/355708/3b79787def0978345fa9ae3b67a2daf3ab89102a/main.c) contains an example on how this FSM can be used
<script src="https://gist.github.com/355708.js?file=main.c"> </script>

PS - If you are reading this post on a blog aggregator  like planet you can view full post [here](http://blog.ankurs.com/2010/04/simple-finite-state-machines-in-c/)

UPDATE - check out the [github repo](https://github.com/ankurs/FSM) for latest code
