====
Poyo
====

|pypi| |pyversions| |license| |travis-ci|

A lightweight YAML Parser for Python

**Please note that Poyo supports only a chosen subset of the YAML format.**

**It can only read but not write and is not compatible with JSON.**

Poyo does not allow deserialization of arbitrary Python objects. Supported
types are **str**, **bool**, **int**, **float**, **NoneType** as well as
**dict** and **list** values. Please see the examples below to get an idea of
what Poyo understands.

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

Poyo is 100% Python and does not require any additional libs.

Usage
-----

Poyo comes with a ``parse_string()`` function, to load utf-8 encoded string
data into a Python dict.

.. code-block:: python

    import codecs
    import logging

    from poyo import parse_string, PoyoException

    logging.basicConfig(level=logging.DEBUG)

    with codecs.open('tests/foobar.yml', encoding='utf-8') as ymlfile:
        ymlstring = ymlfile.read()

    try:
        config = parse_string(ymlstring)
    except PoyoException as exc:
        logging.error(exc)
    else:
        logging.debug(config)

Example
-------

**In (YAML):**

.. code-block:: yaml

    ---
    default_context: # foobar
        greeting: こんにちは
        email: "raphael@hackebrot.de"
        docs: true

        gui: FALSE
        123: 456.789
        # comment
        # allthethings
        'some:int': 1000000
        foo: "hallo #welt" #Inline comment :)
        trueish: Falseeeeeee
        relative-root: /          # web app root path (default: '')
        lektor: 0.0.0.0:5000      # local build
        doc_tools:
            # docs or didn't happen
            -    mkdocs
            - 'sphinx'

            - null
        # 今日は
    zZz: True
    NullValue: Null

    # Block
    # Comment

    Hello World:
        # See you at EuroPython
        null: This is madness   # yo
        gh: https://github.com/{0}.git
    "Yay #python": Cool!

**Out (Python):**

.. code-block:: python

    {
        u'default_context': {
            u'greeting': u'こんにちは',
            u'email': u'raphael@hackebrot.de',
            u'docs': True,
            u'gui': False,
            u'lektor': '0.0.0.0:5000',
            u'relative-root': '/',
            123: 456.789,
            u'some:int': 1000000,
            u'foo': u'hallo #welt',
            u'trueish': u'Falseeeeeee',
            u'doc_tools': [u'mkdocs', u'sphinx', None],
        },
        u'zZz': True,
        u'NullValue': None,
        u'Hello World': {
            None: u'This is madness',
            u'gh': u'https://github.com/{0}.git',
        },
        u'Yay #python': u'Cool!'
    }

Logging
-------

Poyo follows the recommendations for `logging in a library`_, which means it
does **not** configure logging itself. Its root logger is named ``poyo`` and
the names of all its children loggers track the package/module hierarchy. Poyo
logs to a ``NullHandler`` and solely on ``DEBUG`` level.

If your application configures logging and allows debug messages to be shown,
you will see logging when using Poyo. The log messages indicate which parser
method is used for a given string as the parser deseralizes the config. You can
remove all logging from Poyo in your application by setting the log level of
the ``poyo`` logger to a value higher than ``DEBUG``.

**Disable Logging:**

.. code-block:: python

	import logging

	logging.getLogger('poyo').setLevel(logging.WARNING)

**Example Debug Logging Config:**

.. code-block:: python

    import logging
    from poyo import parse_string

    logging.basicConfig(level=logging.DEBUG)

    CONFIG = """
    ---
    default_context: # foobar
        greeting: こんにちは
        gui: FALSE
        doc_tools:
            # docs or didn't happen
            -    mkdocs
            - 'sphinx'
        123: 456.789
    """

    logging.debug(parse_string(CONFIG))

**Example Debug Logging Messages:**

.. code-block:: text

    DEBUG:poyo.parser:parse_blankline <- \n
    DEBUG:poyo.parser:parse_blankline -> IGNORED
    DEBUG:poyo.parser:parse_dashes <- ---\n
    DEBUG:poyo.parser:parse_dashes -> IGNORED
    DEBUG:poyo.parser:parse_section <- default_context: # foobar\n
    DEBUG:poyo.parser:parse_str <- default_context
    DEBUG:poyo.parser:parse_str -> default_context
    DEBUG:poyo.parser:parse_section -> <Section name: default_context>
    DEBUG:poyo.parser:parse_simple <-     greeting: \u3053\u3093\u306b\u3061\u306f\n
    DEBUG:poyo.parser:parse_str <- greeting
    DEBUG:poyo.parser:parse_str -> greeting
    DEBUG:poyo.parser:parse_str <- \u3053\u3093\u306b\u3061\u306f
    DEBUG:poyo.parser:parse_str -> \u3053\u3093\u306b\u3061\u306f
    DEBUG:poyo.parser:parse_simple -> <Simple name: greeting, value: \u3053\u3093\u306b\u3061\u306f>
    DEBUG:poyo.parser:parse_simple <-     gui: FALSE\n
    DEBUG:poyo.parser:parse_str <- gui
    DEBUG:poyo.parser:parse_str -> gui
    DEBUG:poyo.parser:parse_false <- FALSE
    DEBUG:poyo.parser:parse_false -> False
    DEBUG:poyo.parser:parse_simple -> <Simple name: gui, value: False>
    DEBUG:poyo.parser:parse_list <-     doc_tools:\n        # docs or didn't happen\n        -    mkdocs\n        - 'sphinx'\n
    DEBUG:poyo.parser:parse_str <- mkdocs
    DEBUG:poyo.parser:parse_str -> mkdocs
    DEBUG:poyo.parser:parse_str <- 'sphinx'
    DEBUG:poyo.parser:parse_str -> sphinx
    DEBUG:poyo.parser:parse_str <- doc_tools
    DEBUG:poyo.parser:parse_str -> doc_tools
    DEBUG:poyo.parser:parse_list -> <Simple name: doc_tools, value: ['mkdocs', 'sphinx']>
    DEBUG:poyo.parser:parse_simple <-     123: 456.789\n
    DEBUG:poyo.parser:parse_int <- 123
    DEBUG:poyo.parser:parse_int -> 123
    DEBUG:poyo.parser:parse_float <- 456.789
    DEBUG:poyo.parser:parse_float -> 456.789
    DEBUG:poyo.parser:parse_simple -> <Simple name: 123, value: 456.789>
    DEBUG:poyo.parser:parse_simple <-     docs: true\n
    DEBUG:poyo.parser:parse_str <- docs
    DEBUG:poyo.parser:parse_str -> docs
    DEBUG:poyo.parser:parse_true <- true
    DEBUG:poyo.parser:parse_true -> True
    DEBUG:poyo.parser:parse_simple -> <Simple name: docs, value: True>
    DEBUG:root:{'default_context': {'docs': True, 'doc_tools': ['mkdocs', 'sphinx'], 123: 456.789, 'greeting': 'こんにちは', 'gui': False}}

.. _`logging in a library`: https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library


WHY?!
-----

Because a couple of `cookiecutter`_ users, including myself, ran into issues
when installing well-known YAML parsers for Python on various platforms and
Python versions.

.. _`cookiecutter`: https://github.com/audreyr/cookiecutter

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed
description.

.. _`file an issue`: https://github.com/hackebrot/poyo/issues

Code of Conduct
---------------

Everyone interacting in the Poyo project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, poyo is free and open source
software.

.. image:: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
   :align: left
   :alt: OSI certified
   :target: https://opensource.org/

.. _`MIT`: http://opensource.org/licenses/MIT
