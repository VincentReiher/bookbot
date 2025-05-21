from stats import count_words, count_characters, report_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def prettyprint(filepath, num_words, char_count_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in char_count_list:
        if item['char'].isalpha():
            print(f'{item['char']}: {item['num']}')
    print('============= END ===============')


if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_filepath = sys.argv[1]

text = get_book_text(book_filepath)
n_words = count_words(text)
char_count = count_characters(text)
char_count_list = report_characters(char_count)

prettyprint(book_filepath, n_words, char_count_list)

