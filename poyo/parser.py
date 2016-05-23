# -*- coding: utf-8 -*-

import functools
import logging

from ._nodes import Root, Section, Simple, TreeElement
from .exceptions import NoMatchException, NoParentException, NoTypeException

from .patterns import (
    COMMENT, BLANK_LINE, DASHES, LIST, SIMPLE, SECTION,
    LIST_ITEM, NULL, TRUE, FALSE, FLOAT, INT, STR,
)

logger = logging.getLogger(__name__)


def log_callback(wrapped_function):
    @functools.wraps(wrapped_function)
    def _wrapper(parser, match, **kwargs):
        func_name = wrapped_function.__name__
        # Log match group with escaped characters
        matched_string = match.group().encode('unicode_escape').decode()

        logger.debug('{}:{}'.format(func_name, matched_string))
        return wrapped_function(parser, match, **kwargs)
    return _wrapper


class _Parser(object):
    def __init__(self, source):
        self.pos = 0
        self.source = source
        self.max_pos = len(self.source)

        self.root = Root()
        self.seen = [self.root]

        self.rules = (
            (COMMENT, self.parse_comment),
            (BLANK_LINE, self.parse_blankline),
            (DASHES, self.parse_dashes),
            (LIST, self.parse_list),
            (SIMPLE, self.parse_simple),
            (SECTION, self.parse_section),
        )

        self.tag_rules = (
            (NULL, self.parse_null),
            (TRUE, self.parse_true),
            (FALSE, self.parse_false),
            (INT, self.parse_int),
            (FLOAT, self.parse_float),
            (STR, self.parse_str),
        )

    def find_at_level(self, level):
        for candidate in reversed(self.seen):
            if candidate.level < level:
                return candidate
        raise NoParentException(
            'Unable to find element at level {}'.format(level)
        )

    def read_from_tag(self, string):
        for pattern, callback in self.tag_rules:
            match = pattern.match(string)

            if not match:
                continue

            if match.group() != string:
                # Unable to match the full string, try the next pattern
                continue

            return callback(match)

        error_message = 'Unable to determine type for "{}"'
        raise NoTypeException(error_message.format(string))

    @log_callback
    def parse_comment(self, match):
        """Ignore line comments."""

    @log_callback
    def parse_blankline(self, match):
        """Ignore blank lines."""

    @log_callback
    def parse_dashes(self, match):
        """Ignore lines that contain three dash symbols."""

    @log_callback
    def parse_list(self, match):
        groups = match.groupdict()
        level = len(groups['indent'])
        parent = self.find_at_level(level)

        item_matches = LIST_ITEM.findall(groups['items'])

        list_items = [
            self.read_from_tag(value)
            for value in item_matches
        ]

        variable = self.read_from_tag(groups['variable'])
        return Simple(variable, level, list_items, parent=parent)

    @log_callback
    def parse_simple(self, match):
        groups = match.groupdict()

        level = len(groups['indent'])
        parent = self.find_at_level(level)

        variable = self.read_from_tag(groups['variable'])
        value = self.read_from_tag(groups['value'])

        return Simple(variable, level, value, parent=parent)

    @log_callback
    def parse_section(self, match):
        groups = match.groupdict()

        level = len(groups['indent'])
        parent = self.find_at_level(level)

        return Section(
            self.read_from_tag(groups['variable']),
            level,
            parent=parent
        )

    @log_callback
    def parse_null(self, match):
        return None

    @log_callback
    def parse_true(self, match):
        return True

    @log_callback
    def parse_false(self, match):
        return False

    @log_callback
    def parse_int(self, match):
        return int(match.group())

    @log_callback
    def parse_float(self, match):
        return float(match.group())

    @log_callback
    def parse_str(self, match):
        quotes = match.group('quotes')
        return match.group().strip(quotes)

    def __call__(self):
        while self.pos < self.max_pos:
            for pattern, callback in self.rules:
                match = pattern.match(self.source, pos=self.pos)

                if not match:
                    continue

                self.pos = match.end()

                node = callback(match)
                if isinstance(node, TreeElement):
                    self.seen.append(node)

                break
            else:
                raise NoMatchException(
                    'None of the known patterns match for {}'
                    ''.format(self.source[self.pos:])
                )

        return self.root()


def parse_string(string):
    parser = _Parser(string)
    return parser()
