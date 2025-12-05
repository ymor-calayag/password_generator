import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def main():
    password = []

    print("Welcome to the PyPassword Generator!")
    print("---------------")
    num_of_letters = int(input("How many letters would you like in your password?\n"))
    generate_characters(num_of_letters, letters, password)

    num_of_symbols = int(input(f"How many symbols would you like?\n"))
    generate_characters(num_of_symbols, symbols, password)

    num_of_numbers = int(input(f"How many numbers would you like?\n"))
    generate_characters(num_of_numbers, numbers, password)

    print("---------------")
    random.shuffle(password)
    print(f"Your password is: {''.join(password)}")

def generate_characters(char_num, char_list, password):
    count = 0
    while True:
        rand_index = random.randint(0, len(char_list) - 1)
        if count == char_num:
            break
        else:
            password.append(char_list[rand_index])
            count += 1

if __name__ == "__main__":
    main()