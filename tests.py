import unittest
from scheme import Scheme, AmbiguousRequestError
from transliteration import load_scheme, SchemeNameError

class TestScheme(unittest.TestCase):
    def setUp(self):
        self.scheme = Scheme("test")
        self.scheme._register_char('a','b')

    def test_register_char(self):
        self.assertRaises(AmbiguousRequestError, self.scheme._register_char, 'a', 'A')

    def test_convert_char(self):
        self.assertEqual(self.scheme._convert_char('a'), 'b')

if __name__ == '__main__':
    unittest.main()