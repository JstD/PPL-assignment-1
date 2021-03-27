import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Let ;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))