from game import Game


i = True
v = True
b = True
w = int(input("Enter the width of the game board: "))
h = int(input("Enter the height of the game board: "))

# Number for how many players to create
while b == True:
    numPlayers = int(input("How many players will play? "))
    if numPlayers > 0:
        break
    else:
        print("Incorrect input!")
# Number for how many AI Players to create
while v == True:
    AIplayers = int(input("How many Bots would you like to play with? "))
    if AIplayers > 0:
        # Player decides how aggressive the AI Players will be
        difficulty = input("How aggressive should the Bots be: (e)asy or (h)ard? ")
        if difficulty == "e":
            AIrange = w / 2
            break
        elif difficulty == "h":
            AIrange = w / 1.25
            break
        else:
            print("Incorrect input!")
            
    elif AIplayers == 0:
        AIrange = w / 2
        break
    else:
        print("Incorrect input!")

g = Game(w,h,numPlayers,AIplayers,AIrange)
g.play()
end = input("Thanks for Playing... Press enter to exit.")