from tradebook import TradeBook

def get_array_of_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_statement_or_query(line):
    pass

def append_result_to_output_file(result, file_path):
    with open(file_path, 'w') as file:
        return file.write(result)

def main():
    lines = get_array_of_lines_from_file('input_file.txt')
    for line in lines:
        result = line.parse_statement_or_query()
        append_result_to_output_file(result, 'output_file.txt')

if __name__ == "__main__":
    main()