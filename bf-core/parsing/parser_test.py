import unittest
from bf_parser import Parser

class TestMain(unittest.TestCase):
    def parse_simple(self):
        p = Parser()

        ast = p.parse("""
        section Interfaces {}
        """
        )
        print(ast)

        expected_ast = {
            "type": "Specfile",
            "body": [
                {
                    "type": "SECTION",
                    "name": "Interfaces",
                    "body": []
                }
            ]
        }

        self.assertEqual(ast, expected_ast)

unittest.main()