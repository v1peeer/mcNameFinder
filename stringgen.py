from random import choices
import string
import nltk
import os
from nltk.corpus import words

# Download the words corpus if not already downloaded
nltk.download('words')

def generate_random_strings(char_type, num_chars, num_strings):
    """
    Generates random strings based on character type and other parameters.

    Args:
        char_type (int): 1 - Only letters, 2 - Only numbers, 3 - Letters and numbers, 4 - Real words.
        num_chars (int): Number of characters per string.
        num_strings (int): Number of strings to generate.

    Returns:
        set: A set of unique random strings.
    """  
    if char_type == 1:
        chars = string.ascii_lowercase
    elif char_type == 2:
        chars = string.digits
    elif char_type == 3:
        chars = string.ascii_lowercase + string.digits
    elif char_type == 4:
        # Use the function from previous script for real words
        return generate_real_words(num_chars, num_strings)
    else:
        print("Invalid character type. Please choose 1-4.")
        return set()

    random_strings = set()
    max_strings = min(num_strings, (len(chars) ** num_chars))
    while len(random_strings) < max_strings:
        random_string = ''.join(choices(chars, k=num_chars))
        if random_string not in random_strings:
            random_strings.add(random_string)
    return random_strings

def generate_real_words(num_chars, num_strings):
    """
    Generates random real words using the nltk words corpus.

    Args:
        num_chars (int): Number of characters per string (ignored for real words).
        num_strings (int): Number of strings to generate.

    Returns:
        set: A set of unique random real words.
    """  
    word_list = words.words()
    valid_words = set()
    while len(valid_words) < num_strings:
        word = choices(word_list, k=1)[0]
        if len(word) == num_chars:
            valid_words.add(word)
    return valid_words

if __name__ == "__main__":
    while True:
        os.system('cls||clear')
        print("\nstringgen.py")
        print("1. Letters (a-z)")
        print("2. Numbers (0-9)")
        print("3. Letters & Numbers (a-z, 0-9)")
        print("4. Real Words")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            break

        try:
            char_type = int(choice)
            num_chars = int(input("Enter the number of characters per string: "))
            num_strings = int(input("Enter the number of strings to generate: "))

            random_strings = generate_random_strings(char_type, num_chars, num_strings)
            with open("names.txt", "w") as file:
                for random_string in random_strings:
                    file.write(random_string + "\n")
            print(f"Saved {len(random_strings)} strings to names.txt")
        except ValueError:
            print("Invalid input. Please enter integers for your choices.")
