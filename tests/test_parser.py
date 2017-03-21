# -*- coding: utf-8 -*-

import codecs
import pytest

import poyo


@pytest.fixture
def yaml_stream():
    return codecs.open('tests/foobar.yml', encoding='utf-8')


@pytest.fixture
def string_data(yaml_stream):
    return yaml_stream.read()


def test_parse_string(string_data, yaml_stream):
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

    assert poyo.parse_string(string_data) == expected

    yaml_stream.seek(0)
    assert poyo.load(yaml_stream) == expected

    yaml_stream.seek(0)
    assert next(poyo.load_all(yaml_stream)) == expected


def test_yaml_dump():
    with pytest.raises(NotImplementedError):
        poyo.dump({1: 2}, stream=None)
        poyo.dump_all([{1: 2}, {3: 4}], stream=None)
