Getting Started
===============

A scope is basically a dictionary:

.. literalinclude:: examples/a_dict.py
   :language: python
   :emphasize-lines: 4,5


With a speciallty in being used as context manager:

.. literalinclude:: examples/use_with.py
   :language: python
   :emphasize-lines: 4,7


The usage becomes clearer when introducing some functions:

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