# -*- coding: utf-8 -*-

import codecs
import pytest

from poyo import parse_string


@pytest.fixture
def string_data():
    with codecs.open('tests/foobar.yml', encoding='utf-8') as ymlfile:
        return ymlfile.read()


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


@pytest.fixture
def string_data_with_no_newline():
    with codecs.open('tests/no-newline.yml', encoding='utf-8') as ymlfile:
        return ymlfile.read()


def test_parse_string_no_newline(string_data_with_no_newline):
    expected = {
        u'Hello World': {
            u'name': u'Toni Chu',
            u'gh': u'https://github.com/{0}.git',
        },
        u'Yay #python': 3.6,
    }
    assert parse_string(string_data_with_no_newline) == expected


@pytest.fixture
def string_data_list_with_no_newline():
    with codecs.open('tests/no-newline-list.yml', encoding='utf-8') as ymlfile:
        return ymlfile.read()


def test_parse_string_no_newline_list(string_data_list_with_no_newline):
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
    assert parse_string(string_data_list_with_no_newline) == expected
