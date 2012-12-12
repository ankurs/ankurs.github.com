---
comments: true
date: 2009-09-25 01:08:34
layout: post
slug: getting-started-with-pthread
title: Getting started with pthread
wordpress_id: 562
---

Recently i have started coding in C a lot and what i came across from a lot of people is that doing Threading in C is very hard, is it really like that? here is a simple Pthread program that should clear that up

get it [here](http://gist.github.com/179778)

<script src="https://gist.github.com/179778.js?file=thread.c"> </script>

in the above program i have just created 2 threads and passed thr1 ( = 1 ) and thr2 ( = 2 ) values as parameters the function void * thread ( void * ptr ) is executes as a separate thread, we create two thread objects thread1 and thread2, and start threads using pthread\_create function passing thread object, function pointer and parameters as arguments, here NULL specifies default attributes for the thread, we can change this by passing pthread\_attr\_t structure instead of NULL. 

we wait for the threads to finish using the pthread\_join function

One major problem that is faced by most of the people is of using a library which is not a thread safe library, so you need to be careful about the libraries you use in your program, if not sure about a particular library being thread safe, just assume its not thread safe

PS - No updates from a long time as i dont have a proper net connection ....
