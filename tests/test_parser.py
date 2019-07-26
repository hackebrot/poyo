# -*- coding: utf-8 -*-

import codecs
import pytest

from poyo import parse_string


@pytest.fixture
def string_data(ymlfile):
    filename = "tests/{}.yml".format(ymlfile)
    with codecs.open(filename, encoding="utf-8") as fh:
        return fh.read()


@pytest.mark.parametrize("ymlfile", ["foobar"])
def test_parse_string(string_data):
    expected = {
        u"default_context": {
            u"greeting": u"こんにちは",
            u"email": u"raphael@hackebrot.de",
            u"docs": True,
            u"gui": False,
            u"lektor": "0.0.0.0:5000",
            u"relative-root": "/",
            123: 456.789,
            u"some:int": 1000000,
            u"foo": u"hallo #welt",
            u"longtext": (
                u"This is a multiline string. It can contain all "
                u"manners of characters.\nSingle line breaks are "
                u"ignored, but blank linkes cause line breaks.\n"
            ),
            u"trueish": u"Falseeeeeee",
            u"blog": u"raphael.codes",
            u"doc_tools": [u"mkdocs", u"sphinx", None],
        },
        u"zZz": True,
        u"NullValue": None,
        u"Hello World": {
            None: u"This is madness",
            u"gh": u"https://github.com/{0}.git",
        },
        u"Yay #python": u"Cool!",
    }

    assert parse_string(string_data) == expected


@pytest.mark.parametrize("ymlfile", ["no-newline"])
def test_parse_string_no_newline(string_data):
    expected = {
        u"Hello World": {u"name": u"Toni Chu", u"gh": u"https://github.com/{0}.git"},
        u"Yay #python": 3.6,
    }
    assert parse_string(string_data) == expected


@pytest.mark.parametrize("ymlfile", ["no-newline-list"])
def test_parse_string_no_newline_list(string_data):
    expected = {
        u"Hello World": {
            u"numbers": [1, 2],
            u"name": u"Toni Chu",
            u"gh": u"https://github.com/{0}.git",
            u"doc_tools": [u"mkdocs", u"sphinx", None],
        }
    }
    assert parse_string(string_data) == expected


@pytest.mark.parametrize("ymlfile", ["lists"])
def test_parse_string_lists(string_data):
    expected = {u"a": [1, 2], u"b": [3, 4], u"c": [5, 6], u"d": [7, 8]}
    assert parse_string(string_data) == expected


@pytest.mark.parametrize("ymlfile", ["multiline-string"])
def test_parse_multiline_string(string_data):
    import logging

    logging.basicConfig(level=logging.DEBUG)
    expected = {
        u"Hello World": {
            u"multi": (
                u"This is a multiline string. It can contain all manners "
                + u"of characters.\nSingle line breaks are ignored, but blank "
                + u"lines cause line breaks.\n"
            ),
            u"withbreaks": u"Here we will\nkeep our linebreaks\n",
            u"indent": (u"  This has 2 leading spaces and 2 trailing new lines.\n\n"),
            u"chomped": u"Now trailing new line here.",
        }
    }
    assert parse_string(string_data) == expected


@pytest.mark.parametrize('ymlfile', ['list-objects'])
def test_parse_list_objects(string_data):
    expected = {
        u'complicated': {
            u'numbers': [{
                    u'name': u'Hello',
                    u'result': u'World',
                }, {
                    u'name': u'Question',
                    u'result': u'Answer',
                }
            ]
        }
    }
    assert parse_string(string_data) == expected
