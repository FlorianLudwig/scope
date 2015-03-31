Getting Started
===============

What and Why
------------

Scope is a `dependency injection<http://en.wikipedia.org/wiki/Dependency_injection>`_ mechanism for python.
It solves two things:

 * Storing thread-local data in tornado: Somewhere deep down your call stack (within several coroutines) you end up needing the current user name or some request handler.  You may pass these information down the call stack, expanding all function attributes along the way.  Or you inject them.
 * Keepint track of replacable components: Maybe you implement two different login systems and depending on some configuration want to switch that backend.  Injecting the login system instead of importing it where you need it is the scope way to do it.


.. note:: ``Scope`` was written for `tornado<http://www.tornadoweb.org/>`_.  It can be used outside of tornado but it depends on tornado.  The examples are not tornado specific in any way.


In Action
---------

A scope is basically a dictionary:

.. literalinclude:: examples/a_dict.py
   :language: python
   :emphasize-lines: 4,5


So ``'bar'`` is what you want to store and ``'foo'`` is the key where it is stored.  ``'bar'`` might be as well that login system instance, your request handler or current user name.


The `scoping` of `Scope` comes when it is used as context manager:

.. literalinclude:: examples/use_with.py
   :language: python
   :emphasize-lines: 4,7


The usage becomes clearer when introducing some function calls:

.. literalinclude:: examples/use_with2.py
   :language: python
   :emphasize-lines: 2-8,19,20


You might wonder what happens when you enter a scope
inside a scope:  What you expect.  Being nested is
what they where build for.


.. literalinclude:: examples/nested.py
   :language: python


And one final difference you might want to be aware
of compared to a standard dict:

.. literalinclude:: examples/get.py
   :language: python
   :lines: 2-
