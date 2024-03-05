from random import randint

t = ["rock", "paper", "scissors"]

#Computer 
computer = t[randint(0,2)]

def playerChoise():
    player = input("Rock, Paper or Scissors? ")
    return player
