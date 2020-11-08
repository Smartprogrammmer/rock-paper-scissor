import random


# IT display the  player_1 logics
def display():
    global player
    if player == "rock":
        print("player1      :  rock")
    elif player == "paper":
        print("player1      :  paper")
    elif player == "sissier":
        print("player1      :  scissor")


# computer player by random
def comp():
    global com
    global game

    com = random.choice(game)

    print("computer    : ", com)


# point calc

def points():
    global player
    global player1_point
    global com_point

    if player == "rock" and com == "paper":
        com_point = com_point + 1
        print("computer has 1 point= ", com_point)

    elif player == "rock" and com == "scissor":
        player1_point = player1_point + 1
        print("player1 has 1 point= ", player1_point)

    elif player == "scissor" and com == "rock":
        com_point = com_point + 1
        print("computer has 1 point= ", com_point)

    elif player == "scissor" and com == "paper":
        player1_point = player1_point + 1
        print("player1 has 1 point= ", player1_point)

    elif player == "paper" and com == "rock":
        player1_point = player1_point + 1
        print("player has 1 point= ", player1_point)

    elif player == "paper" and com == "scissor":
        com_point = com_point + 1
        print("computer has 1 point= ", com_point)
    else:

        print("no points for both")


# final start the game

def run():
    global number
    global player1_point
    global com_point
    global game
    global player
    player1_point = 0
    com_point = 0
    game = ["rock", "paper", "scissor"]

    while True:
        print(" rock--press--0 paper--press--1  scissor--press--2")

        number = int(input("enter the value :"))

        if number < 3:
            player = game[number]
            display()
            comp()

            points()
            if com_point == 3 or player1_point == 3:
                if com_point == 3:
                    print("")
                    print("**** computer win  match **** ")
                    break
                else:
                    print(" ")
                    print("**** player1 win  the match****")
                    break


        else:
            print(" you enter the worng number")
            print("pls type form 0 to 2\n welcome once agani")


# main of the game
if __name__ == '__main__':
    run()
