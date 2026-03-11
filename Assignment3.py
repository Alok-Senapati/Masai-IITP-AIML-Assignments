CORRECT_PASSWORD = "Python@123"
MAX_ATTEMPTS = 3


def main():
    print("=" * 32)
    print((" " * 7) + "PASSWORD VALIDATOR" + (" " * 7))
    print("=" * 32)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"Attempt {attempt} of {MAX_ATTEMPTS}")
        inp = input("Enter password (or 'quit' to exit): ").strip()
        if inp.lower() == 'quit':
            print("Quiting...")
            break
        if inp != CORRECT_PASSWORD:
            attempts_left = MAX_ATTEMPTS - attempt
            if attempts_left == 0:
                print(f"ACCOUNT LOCKED! Too many failed attempts.")
            else:
                print(f"Incorrect password! {attempts_left} attempts remaining")
                if attempt == 1:
                    print("Hint: Password starts with 'P'")
                else:
                    print("Hint: Password contains '@'")
        else:
            print(f"SUCCESS! Logged in on attempt {attempt}.")
            break
        print()
    print("=" * 32)


if __name__ == '__main__':
    main()