# -*- coding: utf-8 -*-

import re

_INDENT = r"(?P<indent>^ *)"
_VARIABLE = r"(?P<variable>.+):"
_VALUE = r"(?P<value>(?:(?P<q2>['\"]).*?(?P=q2))|[^#]+?)"
_NEWLINE = r"$\n"
_BLANK = r" +"
_INLINE_COMMENT = r"(?: +#.*)?"

_COMMENT = r"^ *#.*" + _NEWLINE
_BLANK_LINE = r"^[ \t]*" + _NEWLINE
_DASHES = r"^---" + _NEWLINE

_SECTION = _INDENT + _VARIABLE + _INLINE_COMMENT + _NEWLINE
_SIMPLE = _INDENT + _VARIABLE + _BLANK + _VALUE + _INLINE_COMMENT + _NEWLINE

_LIST_VALUE = _BLANK + r"-" + _BLANK + _VALUE + _INLINE_COMMENT + _NEWLINE
_LIST_ITEM = _BLANK_LINE + r"|" + _COMMENT + r"|" + _LIST_VALUE

_LIST = _SECTION + r"(?P<items>(?:" + _LIST_ITEM + r")+)"

_NULL = r"\b(null|Null|NULL)\b|~"
_TRUE = r"\b(true|True|TRUE)\b"
_FALSE = r"\b(false|False|FALSE)\b"
_INT = r"[-+]?[0-9]+"
_FLOAT = r"([-+]?(\.[0-9]+|[0-9]+(\.[0-9]*)?)([eE][-+]?[0-9]+)?)"
_STR = r"(?P<quotes>['\"]?).*(?P=quotes)"

# basic rules that the parser matches against
COMMENT = re.compile(_COMMENT, re.MULTILINE)
BLANK_LINE = re.compile(_BLANK_LINE, re.MULTILINE)
DASHES = re.compile(_DASHES, re.MULTILINE)
LIST = re.compile(_LIST, re.MULTILINE)
SIMPLE = re.compile(_SIMPLE, re.MULTILINE)
SECTION = re.compile(_SECTION, re.MULTILINE)

# list rule to retrieve all the individual matches of a list match
LIST_ITEM = re.compile(_LIST_VALUE, re.MULTILINE)

# tag rules to detect types of variable names and value
NULL = re.compile(_NULL)
TRUE = re.compile(_TRUE)
FALSE = re.compile(_FALSE)
FLOAT = re.compile(_FLOAT)
INT = re.compile(_INT)
STR = re.compile(_STR)
