import random
import string as str

def gen_pass(length):
    # Characters to use for password generation
    characters = str.ascii_letters + str.digits + str.punctuation
    
    # Ensure length is valid
    if length < 4:  # Minimum length to include at least one character of each type
        print("Password length must be at least 4 for strong passwords.")
        return None
    
    # Generate a strong password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length (minimum 4): "))
        if length >= 4:
            password = gen_pass(length)
            if password:
                print("\nGenerated Password:")
                print(password)
        else:
            print("Password length too short. Please choose a length of at least 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
