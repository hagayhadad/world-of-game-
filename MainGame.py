from Live import load_game,welcome,GuessGame,MemoryGame,CurrencyGame
from flask import Flask
from MainScores import score_server
name2 = str(input('what is your name?\n'))
welcome(name2)
load_game()
