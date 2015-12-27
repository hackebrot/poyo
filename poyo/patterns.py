# -*- coding: utf-8 -*-

INDENT = r"(?P<indent>^ *)"
VARIABLE = r"(?P<variable>.+):"
VALUE = r"(?P<value>((?P<q2>['\"]).*?(?P=q2))|[^#]+?)"
NEWLINE = r"$\n"
BLANK = r" +"
INLINE_COMMENT = r"( +#.*)?"

COMMENT = r"^ *#.*" + NEWLINE
BLANK_LINE = r"^[ \t]*" + NEWLINE

SECTION = INDENT + VARIABLE + INLINE_COMMENT + NEWLINE
SIMPLE = INDENT + VARIABLE + BLANK + VALUE + INLINE_COMMENT + NEWLINE

NULL = r"null|Null|NULL|~"
TRUE = r"true|True|TRUE"
FALSE = r"false|False|FALSE"
INT = r"[-+]?[0-9]+"
FLOAT = r"([-+]?(\.[0-9]+|[0-9]+(\.[0-9]*)?)([eE][-+]?[0-9]+)?)"
STR = r"(?P<quotes>['\"]?).*(?P=quotes)"
