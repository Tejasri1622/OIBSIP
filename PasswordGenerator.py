import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the length of the password: "))
    use_letters = input("you want letters in your password? (yes/no): ").lower() == 'yes'
    use_numbers = input("you want numbers in your password? (yes/no): ").lower() == 'yes'
    use_symbols = input("you want special symbols in your password? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()
