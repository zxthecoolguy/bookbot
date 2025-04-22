from stats import get_num_words
from stats import count_characters
from stats import sort_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
def get_book_text(path):
    with open(path) as book:
        return book.read()
    
book = get_book_text(book_path)

def main():
    word_count = get_num_words(book)
    chars = count_characters(book)
    sorted_chars = sort_chars(chars)
    
    # Start the report
    report = f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    
    # Add each character count to the report
    for char_dict in sorted_chars:
        char = char_dict["char"]
        # Only include alphabetical characters
        if char.isalpha():
            count = char_dict["count"]
            report += f"\n{char}: {count}"
    
    report += "\n============= END ==============="
    
    print(report)
main()