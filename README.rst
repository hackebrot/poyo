====
Poyo
====

|travis-ci|

A YAML Parser for Python

.. |travis-ci| image:: https://travis-ci.org/hackebrot/poyo.svg?branch=master
    :target: https://travis-ci.org/hackebrot/poyo
    :alt: See Build Status on Travis CI

Usage
-----

.. code-block:: python

    import codecs

    import poyo

    with codecs.open('foobar.yml', encoding='utf-8') as ymlfile:
        config = poyo.parse_string(ymlfile.read())


Example
-------

In:

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

Out:

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
