import re
from tradebook import TradeBook

tradebook = TradeBook()

def get_array_of_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_statement_or_query(line):
    
    pattern1 = "(?P<alien_word>[a-zA-Z]+) is (?P<roman_value>[I|V|X|L|C|D|M])"
    pattern2 = "(?P<value_in_alien>[a-z]+ [a-z]+) (?P<item>[a-zA-Z]+) is (?P<number_of_credits>[0-9]+) Credits"
    pattern3 = "how much is (?P<alien_amount>([a-z]+ )+) ?"
    pattern4 = "how many Credits is (?P<alien_amount>([a-z]+ )+)(?P<item>[a-zA-Z]+) ?"

    if re.match(pattern1, line):
        entry = re.match(pattern1, line)
        alien_word = entry.group('alien_word')
        roman_value = entry.group('roman_value')
        tradebook.conversion_table_alien_to_roman[alien_word] = roman_value

    elif re.match(pattern2, line):
        entry = re.match(pattern2, line)
        value_in_alien = entry.group('value_in_alien')
        item = entry.group('item')
        number_of_credits = entry.group('number_of_credits')
        tradebook.traded_items[item]['value_in_alien'] = value_in_alien
        tradebook.traded_items[item]['number_of_credits'] = number_of_credits
    
    elif re.match(pattern3, line):
        entry = re.match(pattern3, line)
        alien_amount = entry.group('alien_amount')
        value_in_arabic = tradebook.convert_from_alien_to_arabic(alien_amount)
        result_string = alien_amount + ' is ' + str(value_in_arabic)
        return result_string
    
    elif re.match(pattern4, line):
        entry = re.match(pattern4, line)
        alien_amount = entry.group('alien_amount')
        item = entry.group('item')
        tradebook.compute_reference_values_for_items()
        result_credit = tradebook.calculate_number_of_credits_for_given_alien_amount_of_item(alien_amount, item)
        result_string = alien_amount + item + " is " + str(result_credit) + " Credits"
        return result_string
    
    elif len(line) == 0:
        return None

    else:
        result_string = "I have no idea what you are talking about"
        return result_string


def append_result_to_output_file(result, file_path):
    with open(file_path, 'a') as file:
        file.write(result)
        file.write('\n')

def main():
    lines = get_array_of_lines_from_file('input_file.txt')
    for line in lines:
        result = parse_statement_or_query(line)
        if result:
            append_result_to_output_file(result, 'output_file.txt')

if __name__ == "__main__":
    main()