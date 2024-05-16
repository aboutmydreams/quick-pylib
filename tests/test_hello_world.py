from example_lib_name import print_hello_world

import unittest


class TestYourCode(unittest.TestCase):
    def test_result(self):
        result = print_hello_world()
        self.assertEqual(result, "Hello world!", "result fail: expected Hello world!")
