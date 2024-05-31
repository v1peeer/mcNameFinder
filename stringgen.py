import string
import random

def generate_random_strings(num_chars, num_strings):
    chars = string.ascii_lowercase + string.digits
    random_strings = set()
    max_strings = min(num_strings, (len(chars) ** num_chars))
    while len(random_strings) < max_strings:
        random_string = ''.join(random.choice(chars) for _ in range(num_chars))
        if random_string not in random_strings:
            random_strings.add(random_string)
    return random_strings

if __name__ == "__main__":
    num_chars = int(input("Enter the number of characters: "))
    num_strings = int(input("Enter the number of strings to generate: "))
    random_strings = generate_random_strings(num_chars, num_strings)
    with open("names.txt", "w") as file:
        for random_string in random_strings:
            file.write(random_string + "\n")
    print(f"Saved {len(random_strings)} strings to names.txt")
