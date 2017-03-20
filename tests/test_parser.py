# -*- coding: utf-8 -*-

import codecs
import pytest

from poyo import parse_string


@pytest.fixture
def string_data(ymlfile):
    filename = 'tests/{}.yml'.format(ymlfile)
    with codecs.open(filename, encoding='utf-8') as fh:
        return fh.read()


@pytest.mark.parametrize('ymlfile', ['foobar'])
def test_parse_string(string_data):
    expected = {
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

    assert parse_string(string_data) == expected


@pytest.mark.parametrize('ymlfile', ['no-newline'])
def test_parse_string_no_newline(string_data):
    expected = {
        u'Hello World': {
            u'name': u'Toni Chu',
            u'gh': u'https://github.com/{0}.git',
        },
        u'Yay #python': 3.6,
    }
    assert parse_string(string_data) == expected


@pytest.mark.parametrize('ymlfile', ['no-newline-list'])
def test_parse_string_no_newline_list(string_data):
    expected = {
        u'Hello World': {
            u'numbers': [
                1,
                2,
            ],
            u'name': u'Toni Chu',
            u'gh': u'https://github.com/{0}.git',
            u'doc_tools': [
                u'mkdocs',
                u'sphinx',
                None,
            ]
        },
    }
    assert parse_string(string_data) == expected
