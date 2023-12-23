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

class testTransliteration(unittest.TestCase):
    def test_load_scheme(self):
        self.assertRaises(SchemeNameError, load_scheme, "not_a_scheme")
        scheme = load_scheme("test")
        self.assertEqual(scheme.convert("a"), "b")
        self.assertEqual(scheme.convert("azq"), "bwQ")

if __name__ == '__main__':
    unittest.main()