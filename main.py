import string

def count_character_occurrences(file_path: str) -> dict:
    char_count = {}
    
    with open(file_path, "r") as f:
        text = f.read().lower()
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def generate_report(word_count: int, char_counts: dict):
    print("--- Report ---")
    print(f"Number of words: {word_count}")
    print("Character counts:")
    
    for char in sorted(char_counts):
        if char in string.ascii_lowercase:
            print(f"'{char}': {char_counts[char]}")

def main():
    number_of_words = 0
    path_to_file = "/home/maxbraamhaar/workspace/github.com/MaxBraamhaar/bookbot/books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:
        file_contents = f.read()
        lines = file_contents.split()
        number_of_words += len(lines)
    
    char_counts = count_character_occurrences(path_to_file)
    generate_report(number_of_words, char_counts)

if __name__ == "__main__":
    main()