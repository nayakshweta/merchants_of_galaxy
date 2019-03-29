from unittest import TestCase
from tradebook import TradeBook

class TestTradeBook(TestCase):

    def test_tradebook_initialization(self):
        tradebook = TradeBook()

        assert tradebook.traded_items.has_key('Silver')
        assert type(tradebook.traded_items['Silver']) is dict
        assert tradebook.traded_items['Silver']['value_in_alien'] == None
