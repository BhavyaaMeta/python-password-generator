import random

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*"


def generate_password(length):
    password = []

    # Ensure at least one character from each category
    password.append(random.choice(UPPERCASE))
    password.append(random.choice(LOWERCASE))
    password.append(random.choice(DIGITS))
    password.append(random.choice(SPECIAL_CHARACTERS))

    all_characters = (
        UPPERCASE
        + LOWERCASE
        + DIGITS
        + SPECIAL_CHARACTERS
    )

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Randomize character positions
    random.shuffle(password)

    return "".join(password)


def main():

    print("Welcome to Password Generator")

    while True:

        try:
            length = int(
                input("Enter password length (minimum 6): ")
            )
        except ValueError:
            print("Please enter a valid number.")
            continue

        if length < 6:
            print("Password length must be at least 6.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:", password)

        choice = input(
            "\nGenerate another password? (y/n): "
        ).lower()

        if choice != "y":
            print("Thank you for using Password Generator.")
            break


# Run the application only when this file is executed directly
if __name__ == "__main__":
    main()