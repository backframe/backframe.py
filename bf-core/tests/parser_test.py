import unittest

from parsing.parser import Parser

class TestMain(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.p = Parser()

    def test_sections(self):
        ast = self.p.parse("""
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

    def test_variables(self):
        ast = self.p.parse(""" 
        section Interfaces {
            interface Rest {
                isVersioned = true;

                version 1 {
                    
                }
            }

        }   
        """)
        
        expected = {
            "type": "Specfile",
            "sections": [
                {
                    "type": "SECTION",
                    "name": "Interfaces",
                    "body": [
                        {
                            "type": "INTERFACE",
                            "name": "Rest",
                            "body": [
                                {
                                "type": "ASSIGNMENT",
                                "name": "isVersioned",
                                "value": "true"
                                },
                                {
                                    "type": "VERSION",
                                    "name": "1",
                                    "body": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        self.assertEqual(ast, expected)

if __name__ == "__main__":
    unittest.main()