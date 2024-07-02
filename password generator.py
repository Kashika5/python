import random
import string

def generate_password(length):
    # Define the character sets to generate the password from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # includes punctuation symbols

    # Combine all character sets to form the pool of characters to choose from
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.sample(all_characters, length))

    return password

def main():
    print("Welcome to Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Password length should be greater than zero.")
                continue
            
            password = generate_password(length)
            print(f"Generated Password: {password}")

            choice = input("Do you want to generate another password? (yes/no): ").lower()
            if choice != 'yes':
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("Thank you for using Password Generator!")

if __name__ == "__main__":
    main()
