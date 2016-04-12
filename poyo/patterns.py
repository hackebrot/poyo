# -*- coding: utf-8 -*-

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

LISTITEM = BLANK + r"-" + BLANK + VALUE + INLINE_COMMENT + NEWLINE
LIST = SECTION + r"(?P<items>(?:(?P=indent)" + LISTITEM + r")+)"

NULL = r"\b(null|Null|NULL|~)\b"
TRUE = r"\b(true|True|TRUE)\b"
FALSE = r"\b(false|False|FALSE)\b"
INT = r"[-+]?[0-9]+"
FLOAT = r"([-+]?(\.[0-9]+|[0-9]+(\.[0-9]*)?)([eE][-+]?[0-9]+)?)"
STR = r"(?P<quotes>['\"]?).*(?P=quotes)"
