# -*- coding: utf-8 -*-
import textwrap

from poyo import parse_string


def test_parse_string():
    yaml = textwrap.dedent(u"""
    ---
    default_context: # foobar

        greeting: こんにちは
        email: "raphael@hackebrot.de"
        docs: true

        gui: FALSE
        123: 456.789
        someint: 1000000
        foo: "hallo #welt" #Inline comment :)
        trueish: Falseeeeeee
        doc_tools:
            -    mkdocs
            - 'sphinx'

            - null

        other_stuff:

            - more
            - stuff

    zZz: True
    NullValue: Null

    # Block
    # Comment

    Hello World:
        null: This is madness   # yo
        gh: https://github.com/{0}.git
    "Yay #python": Cool!
    """)

    expected = {
        u'default_context': {
            u'greeting': u'こんにちは',
            u'email': u'raphael@hackebrot.de',
            u'docs': True,
            u'gui': False,
            123: 456.789,
            u'someint': 1000000,
            u'foo': u'hallo #welt',
            u'trueish': u'Falseeeeeee',
            u'doc_tools': [u'mkdocs', u'sphinx', None],
            u'other_stuff': [u'more', u'stuff'],
        },
        u'zZz': True,
        u'NullValue': None,
        u'Hello World': {
            None: u'This is madness',
            u'gh': u'https://github.com/{0}.git',
        },
        u'Yay #python': u'Cool!'
    }

    assert parse_string(yaml) == expected
