from random import randint

t = ["Rock", "Paper", "Scissors"]

#Computer 
computer = t[randint(0,2)]

def playerChoise():
    player = input("Rock, Paper or Scissors? ")
    return player

def whoWins(player, computer):
    print(computer)
    if player == computer:
        print("Tie!")
    elif player.lower() == "rock":
        if computer.lower() == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player.lower() == "paper":
        if computer.lower() == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player.lower() == "scissors":
        if computer.lower() == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

def main():
    player = playerChoise()
    whoWins(player, computer)


main()
