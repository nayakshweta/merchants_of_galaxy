from unittest import TestCase
from tradebook import TradeBook

class TestTradeBook(TestCase):

    def test_tradebook_initialization(self):
        tradebook = TradeBook()

        assert tradebook.traded_items.has_key('Silver')
        assert type(tradebook.traded_items['Silver']) is dict
        assert tradebook.traded_items['Silver']['value_in_alien'] == None

    def test_convert_from_roman_to_arabic_I(self):
        tradebook = TradeBook()
        value_in_roman = 'I'
        value_in_arabic = tradebook.convert_from_roman_to_arabic(value_in_roman)

        assert value_in_arabic == 1
    
    def test_convert_from_roman_to_arabic_VI(self):
        tradebook = TradeBook()
        value_in_roman = 'VI'
        value_in_arabic = tradebook.convert_from_roman_to_arabic(value_in_roman)

        assert value_in_arabic == 6

    def test_convert_from_roman_to_arabic_MCMXLIV(self):
        tradebook = TradeBook()
        value_in_roman = 'MCMXLIV'
        value_in_arabic = tradebook.convert_from_roman_to_arabic(value_in_roman)

        assert value_in_arabic == 1944

    def test_convert_from_roman_to_arabic_XXXIX(self):
        tradebook = TradeBook()
        value_in_roman = 'XXXIX'
        value_in_arabic = tradebook.convert_from_roman_to_arabic(value_in_roman)

        assert value_in_arabic == 39
    
    def test_convert_from_roman_to_arabic_MDCL(self):
        tradebook = TradeBook()
        value_in_roman = 'MDCL'
        value_in_arabic = tradebook.convert_from_roman_to_arabic(value_in_roman)

        assert value_in_arabic == 1650
