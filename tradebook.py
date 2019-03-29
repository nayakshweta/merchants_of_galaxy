

class TradeBook:

    def __init__(self):
        self.traded_items = dict.fromkeys(['Silver', 'Gold', 'Iron'])
        
        for key in self.traded_items:
            self.traded_items[key] = dict.fromkeys(['value_in_alien', 'value_in_roman', 'value_in_arabic', 'number_of_credits'])
        
        self.conversion_table_alien_to_roman = {}