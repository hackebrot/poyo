# -*- coding: utf-8 -*-

import re

INDENT = r"(?P<indent>^ *)"
VARIABLE = r"(?P<variable>.+):"
VALUE = r"(?P<value>(?:(?P<q2>['\"]).*?(?P=q2))|[^#]+?)"
NEWLINE = r"$\n"
BLANK = r" +"
INLINE_COMMENT = r"(?: +#.*)?"

COMMENT = r"^ *#.*" + NEWLINE
BLANK_LINE = r"^[ \t]*" + NEWLINE
DASHES = r"^---" + NEWLINE

SECTION = INDENT + VARIABLE + INLINE_COMMENT + NEWLINE
SIMPLE = INDENT + VARIABLE + BLANK + VALUE + INLINE_COMMENT + NEWLINE

LIST_VALUE = BLANK + r"-" + BLANK + VALUE + INLINE_COMMENT + NEWLINE
LIST_ITEM = BLANK_LINE + r"|" + COMMENT + r"|" + LIST_VALUE

LIST = SECTION + r"(?P<items>(?:" + LIST_ITEM + r")+)"

NULL = r"\b(null|Null|NULL|~)\b"
TRUE = r"\b(true|True|TRUE)\b"
FALSE = r"\b(false|False|FALSE)\b"
INT = r"[-+]?[0-9]+"
FLOAT = r"([-+]?(\.[0-9]+|[0-9]+(\.[0-9]*)?)([eE][-+]?[0-9]+)?)"
STR = r"(?P<quotes>['\"]?).*(?P=quotes)"

# basic rules that the parser matches against
COMMENT_CP = re.compile(COMMENT, re.MULTILINE)
BLANK_LINE_CP = re.compile(BLANK_LINE, re.MULTILINE)
DASHES_CP = re.compile(DASHES, re.MULTILINE)
LIST_CP = re.compile(LIST, re.MULTILINE)
SIMPLE_CP = re.compile(SIMPLE, re.MULTILINE)
SECTION_CP = re.compile(SECTION, re.MULTILINE)

# list rule to retrieve all the individual matches of a list match
LISTITEM_CP = re.compile(LIST_VALUE, re.MULTILINE)

# tag rules to detect types of variable names and value
NULL_CP = re.compile(NULL)
TRUE_CP = re.compile(TRUE)
FALSE_CP = re.compile(FALSE)
FLOAT_CP = re.compile(FLOAT)
INT_CP = re.compile(INT)
STR_CP = re.compile(STR)
