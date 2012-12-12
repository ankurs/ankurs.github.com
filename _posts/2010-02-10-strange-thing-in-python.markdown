---
comments: true
date: 2010-02-10 18:22:17
layout: post
slug: strange-thing-in-python
title: strange thing in python
wordpress_id: 599
---

i recently noticed this anyone has a proper explanation for this

for literals i get this

    >>> def a():
    ...     b = []
    ...     c = {}
    ...
    >>> import dis
    >>> dis.dis(a)
    2 0 BUILD_LIST               0
    3 STORE_FAST               0 (b)
    3 6 BUILD_MAP                0
    9 STORE_FAST               1 (c)
    12 LOAD_CONST               0 (None)
    15 RETURN_VALUE

but for constructors i get this

    >>> def a():
    ...     b = list()
    ...     c = dict()
    ...
    >>> dis.dis(a)
    2  0 LOAD_GLOBAL              0 (list)
    3 CALL_FUNCTION            0
    6 STORE_FAST               0 (b)
    3  9 LOAD_GLOBAL              1 (dict)
    12 CALL_FUNCTION            0
    15 STORE_FAST               1 (c)
    18 LOAD_CONST               0 (None)
    21 RETURN_VALUE

i mean why the difference, i was thinking {} and dict() do the same thing, shouldn't they?

