import re

Spec = [
    # Whitespace and comments
    [r"^\s+", None],
    [r"^\#.*", None],

    # Symbols
    [r"^;", ";"],
    [r"^:", ":"],
    [r"^\{", "{"],
    [r"^\}", "}"],
    [r"^\[", "["],
    [r"^\]", "]"],

    # Strings
    [r'^"[^"]*"', "STRING"],
    [r"^'[^']*'", "STRING"],

    # Ops
    [r"^=", "ASSIGNMENT_OP"],
    [r"^,", "COMMA"],
    [r"^\btrue\b", "BOOLEAN"],
    [r"^\bfalse\b", "BOOLEAN"],
    [r"^\w+\('[^']*'\)", "CALL_EXPRESSION"],
    [r'^\w+\("[^"]*"\)', "CALL_EXPRESSION"],

    # Keywords
    [r"^\bsection\b", "SECTION"],
    [r"^\bprovider\b", "PROVIDER"],
    [r"^\binterface\b", "INTERFACE"],
    [r"^\bdatabase\b", "DATABASE"],
    [r"^\bintegration\b", "INTEGRATION"],
    [r"^\bresource\b", "RESOURCE"],
    [r"^\bmethod\b", "METHOD"],
    [r"^\bmigration\b", "MIGRATION"],
    [r"^\bversion\b", "VERSION"],


    # Identifier
    [r"^\w+", "IDENTIFIER"],

]

class Token:
    def __init__(self, _t: str, value: str) -> None:
        self._type = _t
        self.value = value
       

class Tokenizer:
    def __init__(self, val: str) -> None:
        self._cursor = 0
        self._string = val
        self.line = 0
        self.column = 0

    def has_more_tokens(self):
        return self._cursor < len(self._string)

    def is_eof(self):
        return self._cursor == len(self._string)

    def get_next_token(self):
        if not self.has_more_tokens():
            return None

        val = self._string[self._cursor:]
        for (regex, _type) in Spec:
            regex = re.compile(regex)
            value = self._match(regex, val)

            if value == None:
                continue

            if _type == None:
                return self.get_next_token()
            else:
                return Token(_type, value)

        # if no matches
        raise SyntaxError(f"On line: {self.line}, column: {self.column}. unexpected token: `{val[0]}`")
            

    def _match(self, regex: re.Pattern, val: str):
        matched = regex.findall(val)
        if len(matched) == 0:
            return None

        value: str = matched[0]
        new_lines = value.count("\n")
        self._cursor += len(value)
        
        self.line += new_lines
        if new_lines > 0:
            self.column = 0
        self.column += len(value.lstrip())
        

        return value