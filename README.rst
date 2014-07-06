stringlike
==========

|Build Status| |Coverage Status| |PyPi package| |PyPi downloads|

A Python library for implementing string-like classes and lazy strings.

Installation
------------

``stringlike`` is available from
`PyPI <http://pypi.python.org/pypi/stringlike>`__.

To install:

::

    $ pip install stringlike

Or from the source:

::

    $ python setup.py install

Usage
-----

To implement your own ``StringLike`` class, inherit from ``StringLike``
and implement the ``__str__`` magic function, like this:

::

    from stringlike import StringLike

    class StringyThingy(StringLike):
        def __str__(self):
            return "A string representation of my class."

Use the provided lazy string implementations like this:

::

    from stringlike.lazy import LazyString, CachedLazyString

    print "This was lazily {str}".format(str=LazyString(lambda: "generated"))
    print "This is {str}".format(str=CachedLazyString(lambda: "cached"))

A more detailed example can be found
`here <http://developer.covenanteyes.com/stringlike-in-python/>`__.

Unit Tests
----------

To run the unit tests, do this:

::

    $ python tests/run_tests.py

To see the latest test results, check out ``stringlike``'s `Travis CI
page <http://travis-ci.org/#!/CovenantEyes/py_stringlike>`__.

Acknowledgements
----------------

Special thanks to `Eric Shull <https://github.com/exupero>`__ for much
Python help!

License
-------

This package is released under the `MIT
License <http://www.opensource.org/licenses/mit-license.php>`__. (See
LICENSE.txt.)

.. |Build Status| image:: http://img.shields.io/travis/CovenantEyes/py_stringlike.svg?style=flat&branch=master
   :target: https://travis-ci.org/CovenantEyes/py_stringlike
.. |Coverage Status| image:: http://img.shields.io/coveralls/CovenantEyes/py_stringlike.svg?style=flat&branch=master
   :target: https://coveralls.io/r/CovenantEyes/py_stringlike?branch=master
.. |PyPi package| image:: http://img.shields.io/pypi/v/stringlike.svg?style=flat
   :target: http://badge.fury.io/py/stringlike/
.. |PyPi downloads| image::  http://img.shields.io/pypi/dm/stringlike.svg?style=flat
   :target: https://crate.io/packages/stringlike/
