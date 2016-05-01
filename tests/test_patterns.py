# -*- coding: utf-8 -*-

import pytest

from poyo import patterns


def test_COMMENT_matches_a_comment_line():
    match = patterns.COMMENT.match('# baz\n - bar\nfoobar',)
    assert match is not None
    assert match.group() == '# baz\n'


def test_COMMENT_matches_a_comment_line_with_leading_whitespace():
    match = patterns.COMMENT.match('    # baz\n - bar\nfoobar',)
    assert match is not None
    assert match.group() == '    # baz\n'


def test_BLANK_LINE_matches_a_blank_line():
    match = patterns.BLANK_LINE.match('  \nfoobar')
    assert match is not None
    assert match.group() == '  \n'


def test_DASHES_matches_document_separator():
    match = patterns.DASHES.match('---\nfoobar')
    assert match is not None
    assert match.group() == '---\n'


def test_LIST_matches_a_list():
    match = patterns.LIST.match('hmm:\n  - foo\n - "bar"\n    - 123\n-bing')
    assert match is not None
    assert match.group() == 'hmm:\n  - foo\n - "bar"\n    - 123\n'

    groups = match.groupdict()
    assert groups['indent'] == ''
    assert groups['items'] == '  - foo\n - "bar"\n    - 123\n'
    assert groups['variable'] == 'hmm'


def test_LIST_matches_a_list_with_blank_lines():
    match = patterns.LIST.match(
        'hmm:\n  - foo\n\n    - "bar"\n    - 123\n-bing'
    )
    assert match is not None
    assert match.group() == 'hmm:\n  - foo\n\n    - "bar"\n    - 123\n'

    groups = match.groupdict()
    assert groups['indent'] == ''
    assert groups['items'] == '  - foo\n\n    - "bar"\n    - 123\n'
    assert groups['variable'] == 'hmm'


def test_LISTITEM_finds_all_listitems():
    found = patterns.LIST_ITEM.findall(' - foo # baz\n - bar\nfoobar',)
    expected = [
        ('foo', ''),
        ('bar', ''),
    ]
    assert found is not None
    assert found == expected


def test_LISTITEM_finds_all_listitems_with_blank_lines():
    found = patterns.LIST_ITEM.findall(' - foo # baz\n\n - bar\nfoobar',)
    expected = [
        ('foo', ''),
        ('bar', ''),
    ]
    assert found is not None
    assert found == expected


def test_SIMPLE_matches_a_simple_key_value_line():
    match = patterns.SIMPLE.match('   foo: bar # baz\n - bar\nfoobar',)
    assert match is not None
    assert match.group() == '   foo: bar # baz\n'

    groups = match.groupdict()
    assert groups['indent'] == '   '
    assert groups['variable'] == 'foo'
    assert groups['value'] == 'bar'


def test_SECTION_matches_a_section_key_line():
    match = patterns.SECTION.match('   foo: # baz\n      - bar\nfoobar',)
    assert match is not None
    assert match.group() == '   foo: # baz\n'

    groups = match.groupdict()
    assert groups['indent'] == '   '
    assert groups['variable'] == 'foo'


@pytest.mark.parametrize('null_value', ['null', 'Null', 'NULL', '~'])
def test_NULL_matches_a_null_value(null_value):
    match = patterns.NULL.match(null_value)
    assert match is not None
    assert match.group() == null_value


@pytest.mark.parametrize('true_value', ['true', 'True', 'TRUE'])
def test_TRUE_matches_a_true_value(true_value):
    match = patterns.TRUE.match(true_value)
    assert match is not None
    assert match.group() == true_value


@pytest.mark.parametrize('false_value', ['false', 'False', 'FALSE'])
def test_FALSE_matches_a_false_value(false_value):
    match = patterns.FALSE.match(false_value)
    assert match is not None
    assert match.group() == false_value


@pytest.mark.parametrize('float_value', ['1.0', '42.820308', '39.2234e9'])
def test_FLOAT_matches_a_float_value(float_value):
    match = patterns.FLOAT.match(float_value)
    assert match is not None
    assert match.group() == float_value


@pytest.mark.parametrize('int_value', ['1', '42', '3922349'])
def test_INT_matches_an_int_value(int_value):
    match = patterns.INT.match(int_value)
    assert match is not None
    assert match.group() == int_value


def test_STR_matches_a_string_value():
    match = patterns.STR.match('foo bar baz ')
    assert match is not None
    assert match.group() == 'foo bar baz '

    groups = match.groupdict()
    assert groups['quotes'] == ''


def test_STR_matches_a_single_quoted_string_value():
    match = patterns.STR.match("'foo bar baz'   ")

    assert match is not None
    assert match.group() == "'foo bar baz'"

    groups = match.groupdict()
    assert groups['quotes'] == "'"


def test_STR_matches_a_double_quoted_string_value():
    match = patterns.STR.match('"foo bar baz" ')

    assert match is not None
    assert match.group() == '"foo bar baz"'

    groups = match.groupdict()
    assert groups['quotes'] == '"'
