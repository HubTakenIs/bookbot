from stats import word_count, character_count, report
import sys


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = args[1]
    dict = character_count(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print('----------- Word Count ----------')
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    r = report(dict)
    for d in r:
        char = d['char']
        count = d['count']
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue
    print('============= END ===============')

    


main()