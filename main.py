from random import randint
from tkinter import *


t = ["Rock", "Paper", "Scissors"]

#Computer 
computer = t[randint(0,2)]

def playerChoise():
    player = input("Rock, Paper or Scissors? ")
    return player

def whoWins(player, computer):
    #Codigo