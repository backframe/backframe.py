import unittest
import bf_parser

class TestMain(unittest.TestCase):
    def test_parse_simple(self):
        p = bf_parser.Parser()

        ast = p.parse("""
        section Interfaces {}
        """
        )

        expected_ast = {
            "type": "Specfile",
            "sections": [
                {
                    "type": "SECTION",
                    "name": "Interfaces",
                    "body": []
                }
            ]
        }

        self.assertEqual(ast, expected_ast)

    def test_parse_complex(self):
        pass

if __name__ == "__main__":
    unittest.main()