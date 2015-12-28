====
Poyo
====

|pypi| |pyversions| |license| |travis-ci|

A YAML Parser for Python

.. |pypi| image:: https://img.shields.io/pypi/v/poyo.svg
   :target: https://pypi.python.org/pypi/poyo
   :alt: PyPI Package

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/poyo.svg
   :target: https://pypi.python.org/pypi/poyo/
   :alt: PyPI Python Versions

.. |license| image:: https://img.shields.io/pypi/l/poyo.svg
   :target: https://pypi.python.org/pypi/poyo
   :alt: PyPI Package License

.. |travis-ci| image:: https://travis-ci.org/hackebrot/poyo.svg?branch=master
    :target: https://travis-ci.org/hackebrot/poyo
    :alt: See Build Status on Travis CI

Installation
------------

**poyo** is available for download from `PyPI`_ via `pip`_::

    $ pip install poyo

.. _`PyPI`: https://pypi.python.org/pypi
.. _`pip`: https://pypi.python.org/pypi/pip/

**Poyo is 100% Python and does not require any additional libs.**

Usage
-----

Poyo comes with a neat function, named ``parse_string()``, to parse string data
into a Python dict.

.. code-block:: python

    import codecs

    import poyo

    with codecs.open('foobar.yml', encoding='utf-8') as ymlfile:
        config = poyo.parse_string(ymlfile.read())

Please note that Poyo only supports a limited set of YAML features.

See the example below to get a better idea of what Poyo is able to understand.

Example
-------

In (YAML):

.. code-block:: yaml

    default_context: # foobar
        greeting: こんにちは
        email: "raphael@hackebrot.de"
        docs: true
        gui: FALSE
        123: 456.789
        foo: "hallo #welt" #Make sure to understand inline comments


    # Block
    # Comment

    Hello World:
        null: This is madness #yeah
        gh: https://github.com/{0}.git
    "Yay #python": Cool!

Out (Python):

.. code-block:: python

    {
        u'default_context': {
            u'greeting': u'こんにちは',
            u'email': u'raphael@hackebrot.de',
            u'docs': True,
            u'gui': False,
            123: 456.789,
            u'foo': u'hallo #welt',
        },
        u'Hello World': {
            None: u'This is madness',
            u'gh': u'https://github.com/{0}.git',
        },
        u'Yay #python': u'Cool!'
    }

WHY?!
-----

Because a couple of `cookiecutter`_ users, including myself, ran into issues
when installing well-known YAML parsers for Python on various platforms and
Python versions.

.. _`cookiecutter`: https://github.com/audreyr/cookiecutter

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/hackebrot/poyo/issues

Code of Conduct
---------------

Everyone interacting in the Poyo project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, poyo is free and open source software

.. _`MIT`: http://opensource.org/licenses/MIT
