import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, guess):
        if guess == self.secret_number:
            print("Congratulations! You guessed the correct number.")
            return True
        elif guess < self.secret_number:
            print("Too low. Try again.")
            return False
        else:
            print("Too high. Try again.")
            return False

    def play(self):
        self.generate_number()
        while True:
            guess = self.get_guess_from_user()
            if self.compare_results(guess):
                return True



