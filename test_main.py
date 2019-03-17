import unittest
from main import sprich_zahl


class TestMain(unittest.TestCase):
    def test_some_numbers(self):
        examples = {1: "eins",
                    11: "elf",
                    19: "neunzehn",
                    21: "einundzwanzig",
                    1000000: "eine Million",
                    10000001: "zehn Millionen eins",
                    987654321: "neunhundertsiebenundachtzig Millionen sechshundertvierundfünfzigtausend dreihunderteinundzwanzig"}

        for zahl, text in examples.items():
            with self.subTest(zahl=zahl, text=text):
                self.assertEqual(sprich_zahl(zahl), text)

    def test_zero(self):
        self.assertEqual(sprich_zahl(0), "null")

    def test_negative(self):
        examples = {-1: "minus eins",
                    -1109: "minus eintausend einhundertneun"}

        for zahl, text in examples.items():
            with self.subTest(zahl=zahl, text=text):
                self.assertEqual(sprich_zahl(zahl), text)

