import unittest
from my_program import print_my_program


class TestPrintMyProgram(unittest.TestCase):

    def test_print_my_program(self):
        result = print_my_program()
        self.assertEqual(result, "Hello my program!")


if __name__ == "__main__":
    unittest.main()
