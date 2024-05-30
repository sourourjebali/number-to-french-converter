import unittest
from src.converter import convert_to_french, convert_list

class TestNumberToFrenchConverter(unittest.TestCase):
    def test_units(self):
        self.assertEqual(convert_to_french(0), "zéro")
        self.assertEqual(convert_to_french(5), "cinq")
        self.assertEqual(convert_to_french(16), "seize")

    def test_tens(self):
        self.assertEqual(convert_to_french(21), "vingt-et-un")
        self.assertEqual(convert_to_french(35), "trente-cinq")
        self.assertEqual(convert_to_french(99), "quatre-vingt-dix-neuf")

    def test_hundreds(self):
        self.assertEqual(convert_to_french(100), "cent")
        self.assertEqual(convert_to_french(123), "cent-vingt-trois")
        self.assertEqual(convert_to_french(999), "neuf-cent-quatre-vingt-dix-neuf")

    def test_thousands(self):
        self.assertEqual(convert_to_french(1000), "mille")
        self.assertEqual(convert_to_french(2001), "deux-mille-un")
        self.assertEqual(convert_to_french(12345), "douze-mille-trois-cent-quarante-cinq")

    def test_convert_list(self):
        numbers = [0, 1, 20, 21, 35, 99, 100, 101, 999, 1000, 1001, 1111]
        expected = ["zéro", "un", "vingt", "vingt-et-un", "trente-cinq", "quatre-vingt-dix-neuf", "cent", "cent-un", "neuf-cent-quatre-vingt-dix-neuf", "mille", "mille-un", "mille-cent-onze"]
        self.assertEqual(convert_list(numbers), expected)



if __name__ == '__main__':
    unittest.main()