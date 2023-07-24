import random
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyGame import CurrencyGame
from Score import add_score,first_score
from MainScores import score_server
from Utils import screen_cleaner
import requests

def playagain():
    play_again=str(input("do you want to play again?(y/n).\n"))
    if play_again=='y':
        load_game()
    if play_again=='n':
        print("finish")
    else:
        print("please choose y if you want to play again or n if you want to finish")

def welcome(name):
    first_score()
 #   mainscore()
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    while True:
        try:
            global gamenum
            gamenum = int(input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
        except ValueError:
           print("You have entered an invalid value.")
           continue
        if 0 < gamenum <=3:
            break
        else:
            print('Valid range, please: 1-3')
    while True:
        try:
            global level
            level = int(input("Please choose game difficulty from 1 to 5:\n"))
        except ValueError:
           print("You have entered an invalid value.")
           continue
        if 0 < level <=5:
            break
        else:
            print('Valid range, please: 1-5')
    if gamenum == 2:
        difficulty = level
        game = GuessGame(difficulty)
        if game.play():
            add_score(difficulty)
    if gamenum == 1:
        difficulty = level
        game = MemoryGame(difficulty)
        result = game.play()
        if result:
            print("Congratulations! You won.")
            add_score(difficulty)
        else:
            print("Sorry, you lost.")
    if gamenum == 3:
        difficulty = level
        game = CurrencyGame(difficulty)
        if game.play_game():
            add_score(difficulty)
    screen_cleaner()
    playagain()


