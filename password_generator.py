import random


class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        print("Welcome to the PyPassword Generator!")
        self.nr_letters = int(input("How many letters would you like in your password?\n"))
        self.nr_symbols = int(input("How many symbols would you like?\n"))
        self.nr_numbers = int(input("How many numbers would you like?\n"))

        self.password_list = []
        for _ in range(self.nr_letters):
            self.password_list.append(random.choice(self.letters))
        for _ in range(self.nr_symbols):
            self.password_list.append(random.choice(self.symbols))
        for _ in range(self.nr_numbers):
            self.password_list.append(random.choice(self.numbers))

        random.shuffle(self.password_list)

        password = "".join(self.password_list)
        print(f"Your password is: {password}")


# Create an instance of PasswordGenerator to run the code
generator = PasswordGenerator()
