from tradebook import TradeBook

def get_array_of_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def main():
    lines = get_array_of_lines_from_file('input_file.txt')
    for line in lines:
        line.parse_statement_or_query()

if __name__ == "__main__":
    main()