# -*- coding: utf-8 -*-
from ._nodes import Root, Section, Simple
from .exceptions import NoMatchException, NoParentException, NoTypeException
from .patterns import (
    BLANK_LINE_CP, COMMENT_CP, DASHES_CP, FALSE_CP, FLOAT_CP, INT_CP,
    LIST_CP, LISTITEM_CP, NULL_CP, SECTION_CP, SIMPLE_CP, STR_CP, TRUE_CP,
)


class _Parser(object):
    def __init__(self, source):
        self.pos = 0
        self.source = source
        self.max_pos = len(self.source)

        self.root = Root()
        self.seen = [self.root]

        self.rules = (
            (COMMENT_CP, self.parse_comment),
            (BLANK_LINE_CP, self.parse_blankline),
            (DASHES_CP, self.parse_dashes),
            (LIST_CP, self.parse_list),
            (SIMPLE_CP, self.parse_simple),
            (SECTION_CP, self.parse_section),
        )

        self.tag_rules = (
            (NULL_CP, self.parse_null),
            (TRUE_CP, self.parse_true),
            (FALSE_CP, self.parse_false),
            (FLOAT_CP, self.parse_float),
            (INT_CP, self.parse_int),
            (STR_CP, self.parse_str),
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
                raise ValueError
            return callback(match)

        raise NoTypeException(
            'Unable to determine type for "{}"'.format(string)
        )

    def parse_comment(self, match):
        pass

    def parse_blankline(self, match):
        pass

    def parse_dashes(self, match):
        pass

    def parse_list(self, match):
        groups = match.groupdict()
        level = len(groups['indent'])
        parent = self.find_at_level(level)

        item_matches = LISTITEM_CP.findall(groups['items'])

        list_items = [
            self.read_from_tag(value)
            for value, _ in item_matches
        ]

        simple = Simple(
            self.read_from_tag(groups['variable']),
            level,
            list_items,
            parent=parent
        )
        self.seen.append(simple)

    def parse_simple(self, match):
        groups = match.groupdict()

        level = len(groups['indent'])
        parent = self.find_at_level(level)

        simple = Simple(
            self.read_from_tag(groups['variable']),
            level,
            self.read_from_tag(groups['value']),
            parent=parent
        )
        self.seen.append(simple)

    def parse_section(self, match):
        groups = match.groupdict()

        level = len(groups['indent'])
        parent = self.find_at_level(level)

        section = Section(
            self.read_from_tag(groups['variable']),
            level,
            parent=parent
        )
        self.seen.append(section)

    def parse_null(self, match):
        return None

    def parse_true(self, match):
        return True

    def parse_false(self, match):
        return False

    def parse_int(self, match):
        return int(match.group())

    def parse_float(self, match):
        return float(match.group())

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
                callback(match)
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
