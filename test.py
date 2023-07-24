# import random
# import requests
#
# class CurrencyGame:
#     def __init__(self,difficulty):
#         self.difficulty = difficulty
#
#     def get_money_interval(self):
#         try:
#             response = requests.get(
#                 "https://openexchangerates.org/api/latest.json?app_id=cea86b4c3d7943a29901a94cf8781401&base=USD&symbols=ILS")
#             response.raise_for_status()  # Check for any HTTP errors
#             data = response.json()
#             exchange_rate = data['rates']["ILS"]
#             total_value = random.randint(1, 100)
#             lower_bound = total_value * exchange_rate - (5 - self.difficulty)
#             upper_bound = total_value * exchange_rate + (5 - self.difficulty)
#             print (exchange_rate,total_value,lower_bound,upper_bound)
#             return lower_bound, upper_bound, total_value, exchange_rate
#         except (requests.exceptions.RequestException, ValueError, KeyError) as e:
#             print(f"An error occurred while retrieving the exchange rate: {e}")
#             # Provide a default exchange rate if an error occurs
#             exchange_rate = 3.5  # Set your desired default exchange rate
#             total_value = random.randint(1, 100)
#             lower_bound = total_value * exchange_rate - (5 - self.difficulty)
#             upper_bound = total_value * exchange_rate + (5 - self.difficulty)
#             return lower_bound, upper_bound, total_value, exchange_rate
#
#     def get_guess_from_user(self, total_value, exchange_rate):
#         usd_value = input(f"Guess the value of {total_value} USD in ILS: \n")
#         try:
#             usd_value = float(usd_value)
#            # ils_value = usd_value * exchange_rate
#             return usd_value
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             return None
#
#     def play_game(self):
#         interval_data = self.get_money_interval()
#         if interval_data is None:
#             return False
#         lower_bound, upper_bound, total_value, exchange_rate = interval_data
#         guess = self.get_guess_from_user(total_value, exchange_rate)
#         if guess is None:
#             return False
#         if lower_bound <= guess <= upper_bound:
#             print(f"Congratulations! The correct value was {total_value} USD = {total_value*exchange_rate} ILS.")
#             return True
#         else:
#             print(f"Sorry, the correct value was {total_value*exchange_rate} USD. You guessed {guess} ILS.")
#             return False
#
# # Example usage
# game = CurrencyGame(4)
# game.play_game()

from Score import add_score

add_score(3)

