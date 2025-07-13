
import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters  

    if complexity >= 2:
        characters += string.digits  

    if complexity == 3:
        characters += string.punctuation  

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password (8 or higher): "))
    
    complexity = int(input("Choose complexity level (1 = letters, 2 = letters + numbers, 3 = letters + numbers + symbols): "))
    
    if length < 8 or complexity < 1 or complexity > 3:
        print("Invalid input. Length must be at least 8 and complexity between 1 and 3.")
        return

    password = generate_password(length, complexity)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()