from unittest import TestCase
from merchants_of_galaxy import parse_statement_or_query
import re

class TestMerchantsOfGalaxy(TestCase):

    def test_parse_statement_or_query_pattern1(self):
        line = "glob is I"
        pattern1 = "(?P<alien_word>[a-zA-Z]+) is (?P<roman_value>[I|V|X|L|C|D|M])"
        entry = re.match(pattern=pattern1, string=line)

        assert entry.group('alien_word') == "glob"
        assert entry.group('roman_value') == "I"
    
    def test_parse_statement_or_query_pattern2(self):
        line = "glob glob Silver is 34 Credits"
        pattern2 = "(?P<value_in_alien>[a-z]+ [a-z]+) (?P<item>[a-zA-Z]+) is (?P<number_of_credits>[0-9]+) Credits"
        entry = re.match(pattern=pattern2, string=line)

        assert entry.group('value_in_alien') == "glob glob"
        assert entry.group('item') == "Silver"
        assert entry.group('number_of_credits') == '34'

    def test_parse_statement_or_query_pattern3(self):
        line = "how much is pish tegj glob glob ?"
        pattern3 = "how much is (?P<alien_amount>([a-z]+ )+) ?"
        entry = re.match(pattern=pattern3, string=line)

        assert entry.group('alien_amount') == "pish tegj glob glob "
    
    def test_parse_statement_or_query_pattern4(self):
        line = "how many Credits is glob prok Silver ?"
        pattern4 = "how many Credits is (?P<alien_amount>([a-z]+ )+)(?P<item>[a-zA-Z]+) ?"
        entry = re.match(pattern=pattern4, string=line)

        assert entry.group('alien_amount') == "glob prok "
        assert entry.group('item') == "Silver"
    
