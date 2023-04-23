from game import Game

w = int(input("Enter the width of the game board: "))
h = int(input("Enter the height of the game board: "))

# Number for how many players to create
numPlayers = int(input("How many players will play? "))
# Number for how many AI Players to create
AIplayers = int(input("How many Bots would you like to play with?"))

g = Game(w,h,numPlayers,AIplayers)
g.play()
