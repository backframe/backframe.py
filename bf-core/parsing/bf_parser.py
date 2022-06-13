from tokenizer import Tokenizer, Token


class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, val: str):
        self._string = val
        self._tokenizer = Tokenizer(val)
        self._lookahead = self._tokenizer.get_next_token()

        return {
            "type": "Specfile",
            "sections": self.section_list()
        }

    def section_list(self):
        # Expect at least one section
        sections = [self.section()]

        while self._tokenizer.has_more_tokens():
            sections.append(self.section())

        return sections

    def section(self):
        self._eat("SECTION")
        id = self._eat("IDENTIFIER")
        self._eat("{")

        body = self.statement_list()

        self._eat("}")
        return {
            "type": "SECTION",
            "name": id.value,
            "body": body
        }
    
    def statement_list(self):
        stmnts = []

        while self._lookahead._type != "}":
            stmnts.append(self.statement())

        return stmnts

    def statement(self):
        next = self._lookahead._type
        if next == "IDENTIFIER":
            return self.expression_statement()
        else:
            return self.block_statement()

    def expression_statement(self):
        name = self._eat("IDENTIFIER")
        self._eat("ASSIGNMENT_OP")
        token = self.literal()

        self._eat(";")
        return {
            "type": "ASSIGNMENT",
            "name": name.value,
            "value": token.value
        }


    def literal(self):
        next = self._lookahead._type

        if next == "STRING":
            return self._eat("STRING")
        elif next == "BOOLEAN":
            return self._eat("BOOLEAN")
        elif next == "[":
            return self.array()
        elif next == "{":
            return self.object()
        else:
            return self._eat("STRING")

    def array(self):
        values = []
        self._eat("[")

        while self._lookahead._type != "]":
            tok = self._eat("STRING")
            self._eat("COMMA")
            values.append(tok.value)

        self._eat("]")
        return Token("ARRAY", "|".join(values))

    def object(self):
        values = []
        self._eat("{")

        while self._lookahead._type != "}":
            key = self._eat("IDENTIFIER")
            self._eat(":")
            value = self._eat("IDENTIFIER")
            self._eat("COMMA")
            values.append(f"{key.value}->{value.value}")

        self._eat("}")
        print(";".join(values))
        return Token("OBJECT", ";".join(values))

    # Generic block statement node
    def block_statement(self):
        token = self._lookahead
        name = self._eat(token._type)
        id = self._eat("IDENTIFIER")
        self._eat("{")

        body = self.statement_list()

        self._eat("}")
        return {
            "type": name._type,
            "name": id.value,
            "body": body
        }

    def _eat(self, _type: str):
        token = self._lookahead
        if token._type != _type:
            raise SyntaxError(f"Expected token: {_type} but instead found: {token._type}")
        
        # Advance to next token
        self._lookahead = self._tokenizer.get_next_token()
        return token