# -*- coding: utf-8 -*-

from poyo import patterns


def test_COMMENT_matches_a_comment_line():
    match = patterns.COMMENT.match('# baz\n - bar\nfoobar',)
    assert match is not None
    assert match.group() == '# baz\n'
    assert match.groupdict() == {}


def test_COMMENT_matches_a_comment_line_with_leading_whitespace():
    match = patterns.COMMENT.match('    # baz\n - bar\nfoobar',)
    assert match is not None
    assert match.group() == '    # baz\n'
    assert match.groupdict() == {}


def test_BLANK_LINE_matches_a_blank_line():
    match = patterns.BLANK_LINE.match('  \nfoobar')
    assert match is not None
    assert match.group() == '  \n'


def test_DASHES_matches_document_separator():
    match = patterns.DASHES.match('---\nfoobar')
    assert match is not None
    assert match.group() == '---\n'


def test_LIST_matches_a_list():
    match = patterns.LIST.match('hmm:\n  - foo\n - bar\n    - blah\n-bing')
    assert match is not None
    assert match.group() == 'hmm:\n  - foo\n - bar\n    - blah\n'
    assert match.groupdict() == {
        'variable': 'hmm',
        'items': '  - foo\n - bar\n    - blah\n',
        'indent': '',
    }


def test_LIST_matches_a_list_with_blank_lines():
    match = patterns.LIST.match(
        'hmm:\n  - foo\n\n    - bar\n    - blah\n-bing'
    )
    assert match is not None
    assert match.group() == 'hmm:\n  - foo\n\n    - bar\n    - blah\n'
    assert match.groupdict() == {
        'variable': 'hmm',
        'items': '  - foo\n\n    - bar\n    - blah\n',
        'indent': '',
    }


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
    assert match.groupdict() == {
        'indent': '   ',
        'q2': None,
        'value': 'bar',
        'variable': 'foo',
    }


def test_SECTION_matches_a_section_key_line():
    match = patterns.SECTION.match('   foo: # baz\n      - bar\nfoobar',)
    assert match is not None
    assert match.group() == '   foo: # baz\n'
    assert match.groupdict() == {
        'indent': '   ',
        'variable': 'foo',
    }


def test_NULL_matches_a_null_value():
    for value in ('null', 'Null', 'NULL'):
        match = patterns.NULL.match(value + '   ')
        assert match is not None
        assert match.group() == value
        assert match.groupdict() == {}


def test_TRUE_matches_a_true_value():
    for value in ('true', 'True', 'TRUE'):
        match = patterns.TRUE.match(value + '   ')
        assert match is not None
        assert match.group() == value
        assert match.groupdict() == {}


def test_FALSE_matches_a_false_value():
    for value in ('false', 'False', 'FALSE'):
        match = patterns.FALSE.match(value + '   ')
        assert match is not None
        assert match.group() == value
        assert match.groupdict() == {}


def test_FLOAT_matches_a_float_value():
    for value in ('1.0', '42.820308', '39.2234e9'):
        match = patterns.FLOAT.match(value + '   ')
        assert match is not None
        assert match.group() == value
        assert match.groupdict() == {}


def test_INT_matches_an_int_value():
    for value in ('1', '42', '3922349'):
        match = patterns.INT.match(value + '   ')
        assert match is not None
        assert match.group() == value
        assert match.groupdict() == {}


def test_STR_matches_a_string_value():
    value = 'foo bar baz'
    match = patterns.STR.match(value + '   ')
    assert match is not None
    assert match.group() == value + '   '
    assert match.groupdict() == {
        'quotes': '',
    }


def test_STR_matches_a_single_quoted_string_value():
    value = "'foo bar baz'"
    match = patterns.STR.match(value + '   ')
    assert match is not None
    assert match.group() == value
    assert match.groupdict() == {
        'quotes': "'",
    }


def test_STR_matches_a_double_quoted_string_value():
    value = '"foo bar baz"'
    match = patterns.STR.match(value + '   ')
    assert match is not None
    assert match.group() == value
    assert match.groupdict() == {
        'quotes': '"',
    }
