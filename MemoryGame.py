import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_list = []
        for _ in range(self.difficulty):
            try:
                number = int(input("Enter a number: "))
                user_list.append(number)
            except ValueError:
                print("You have entered an invalid value.")
                continue
        return user_list

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        sequence = self.generate_sequence()
        print("Memorize the numbers:", sequence)
        time.sleep(0.7)
        user_list = self.get_list_from_user()
        return self.is_list_equal(sequence, user_list)

