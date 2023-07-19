import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):

    def test_null_english_to_french(self):
        self.assertEqual('', english_to_french(''))


    def test_null_french_to_english(self):
        self.assertEqual('', french_to_english(''))
        

    def test_hello_english_to_french(self):
        self.assertEqual("bonjour", english_to_french('hello'))
        self.assertNotEqual("bonsoir", english_to_french('hello'))


    def test_bonjour_french_to_english(self):
        self.assertEqual('hello', french_to_english('bonjour'))
        self.assertNotEqual("hello", english_to_french('bonsoir'))


if __name__ == '__main__':
    unittest.main()