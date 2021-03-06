

class TradeBook:

    def __init__(self):
        self.traded_items = dict.fromkeys(['Silver', 'Gold', 'Iron'])
        
        for key in self.traded_items:
            self.traded_items[key] = dict.fromkeys(['value_in_alien', 'value_in_roman', 'value_in_arabic', 'number_of_credits'])
        
        self.conversion_table_alien_to_roman = {}


    def convert_from_roman_to_arabic(self, value_in_roman):
        symbol_to_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        list_of_roman_characters = list(value_in_roman)

        if len(list_of_roman_characters) == 1:
            value_in_arabic = symbol_to_value[value_in_roman]
        else:
            i = 0
            sum = 0
            else_count = 0
            else_sum = 0

            while i < (len(list_of_roman_characters) - 1):
                char = list_of_roman_characters[i]
                next_char = list_of_roman_characters[i + 1]

                if symbol_to_value[char] >= symbol_to_value[next_char]:
                    if else_count != 0:
                        sum = sum + (symbol_to_value[char] - else_sum)
                    else:
                        sum = sum + symbol_to_value[char]
                    else_count = 0
                    else_sum = 0
                else:
                    while else_count <= 3:
                        else_sum = else_sum + symbol_to_value[char]
                        else_count += 1
                        break
                i += 1
            sum = sum + (symbol_to_value[next_char] - else_sum)

            value_in_arabic = sum

        return value_in_arabic


    def convert_from_alien_to_roman(self, value_in_alien):
        list_of_words_in_alien_value = value_in_alien.split()

        total_value_in_roman = ''

        for word in list_of_words_in_alien_value:
            value_of_current_word_in_roman = self.conversion_table_alien_to_roman[word]
            total_value_in_roman = total_value_in_roman + value_of_current_word_in_roman

        return total_value_in_roman

    def convert_from_alien_to_arabic(self, value_in_alien):
        value_in_roman = self.convert_from_alien_to_roman(value_in_alien)
        value_in_arabic = self.convert_from_roman_to_arabic(value_in_roman)
        return value_in_arabic
    
    def compute_reference_values_for_items(self):
        for key in self.traded_items:
            if self.traded_items[key]['value_in_alien']:
                item_dict = self.traded_items[key]
                item_dict['value_in_roman'] = self.convert_from_alien_to_roman(item_dict['value_in_alien'])
                item_dict['value_in_arabic'] = self.convert_from_roman_to_arabic(item_dict['value_in_roman'])
    
    def calculate_number_of_credits_for_given_alien_amount_of_item(self, alien_amount, item):
        amount_in_arabic = self.convert_from_alien_to_arabic(alien_amount)
        item = self.traded_items[item]
        result_credits = int(item['number_of_credits']) * amount_in_arabic / item['value_in_arabic']
        return result_credits