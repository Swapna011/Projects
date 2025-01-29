import random
import string

def password_generator(length, complexity):
    if complexity == "weak":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator Application")
    print("-------------------------------------")

    while True:
        length = int(input("Enter the desired length of the password (8-32): "))
        while length < 8 or length > 32:
            length = int(input("Invalid length. Please enter a value between 8 and 32: "))

        print("Select password complexity:")
        print("1. Weak (lowercase letters)")
        print("2. Medium (letters)")
        print("3. Strong (letters, digits, special characters)")

        choice = input("Enter your choice (1/2/3): ")
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Please enter 1, 2, or 3: ")

        if choice == "1":
            complexity = "weak"
        elif choice == "2":
            complexity = "medium"
        elif choice == "3":
            complexity = "strong"

        password = password_generator(length, complexity)
        print(f"\nGenerated Password: {password}\n")

        again = input("Generate another password? (yes/no): ").lower()
        while again not in ["yes", "no"]:
            again = input("Invalid input. Generate another password? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()
