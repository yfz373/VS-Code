def write_to_file():
    user_input = input("Please enter some text: ")
    with open("user_input.txt", "a") as file:
        file.write(user_input + "\n")

def read_from_file():
    try:
        with open("user_input.txt", "r") as file:
            print("Here is the content of the file:")
            print(file.read())
    except FileNotFoundError:
        print("The file is empty or does not exist.")

def main():
    while True:
        print("Options:")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            write_to_file()
        elif choice == "2":
            read_from_file()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()