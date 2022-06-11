from tokenizer import Tokenizer

class Block:
    def __init__(self, t: str, id: str) -> None:
        self._type = t
        self.id = id
        self.variables = {}
        self.blocks = []


class Parser:
    def __init__(self, string: str) -> None:
        self._string = string

    # TODO: Define productions
    def parse(self, val: str):
        self._string = val
        self._tokenizer = Tokenizer(val)
        self._lookahead = self._tokenizer.get_next_token()

    
    def statement_list(self):
        pass

    def _eat(self, _type: str):
        token = self._lookahead
        if token._type == _type:
            raise SyntaxError("Expected token: {_type} but instead found: {token._type}")
        
        # Advance to next token
        self._lookahead = self._tokenizer.get_next_token()
        return token