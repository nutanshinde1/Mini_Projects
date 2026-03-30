import random
import string

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    length = int(input("Enter password length: "))
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, digits, symbols)

    print("Generated Password:", password)


main()
