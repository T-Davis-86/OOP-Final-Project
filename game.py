from treasure import Treasure
from player import Player
from randomNum import Random
import sys
from randomNum import Random
rand= Random()
from weapon import Weapon
import math
from player import AIPlayer
import random
from os import system, name
from time import sleep
if len(sys.argv) > 1:
  rand.setSeed(int(sys.argv[1]))
def clear():
    if name == 'nt':
        _ = system('cls')
    # Clear screen for mac and linux
    else:
     _ = system('clear')
    # Clear screen for Windows
class Game:
    
    # the constructor (initialize all game variables)
    def __init__(self, width, height,numPlayers,AIplayers,diff):  
        self.gameBoardWidth = width;
        self.gameBoardHeight = height;
        self.listOfPlayers = []
        self.listOfTreasures = []
        self.listOfWeapons = []
        self.difficulty = diff
        p = 1

        # Creating the number of players designated by the user

        for plyrs in range(numPlayers):
            positionx = rand.randrange(self.gameBoardWidth)
            positiony = rand.randrange(self.gameBoardHeight)
            player = Player(positionx,positiony,str(p))
            self.listOfPlayers.append(player)
            p += 1
        
        # Creating the number of AI Players as designated by user

        for number in range(AIplayers):
            positionx = rand.randrange(self.gameBoardWidth)
            positiony = rand.randrange(self.gameBoardHeight) 
            player = AIPlayer(positionx,positiony,str(p))
            self.listOfPlayers.append(player)
            p += 1



        # Creating all the items for the game

        t1 = Treasure("silver","S", 20, rand.randrange(self.gameBoardWidth), rand.randrange(self.gameBoardHeight))
        self.listOfTreasures.append(t1)
        t2 = Treasure("gold","G", 25, rand.randrange(self.gameBoardWidth), rand.randrange(self.gameBoardHeight))
        self.listOfTreasures.append(t2)
        t3 = Treasure("platinum","P",50,rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight))
        self.listOfTreasures.append(t3)
        t4 = Treasure("diamond","D",40,rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight))
        self.listOfTreasures.append(t4)
        t5 = Treasure("emerald","E",35,rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight))
        self.listOfTreasures.append(t5)
        if numPlayers > 3:
            w1 = Weapon("gun", "/", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 7)
            self.listOfWeapons.append(w1)
            w2 = Weapon("grenade", "o", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 4)
            self.listOfWeapons.append(w2)
            w1 = Weapon("gun", "/", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 7)
            self.listOfWeapons.append(w1)
            w2 = Weapon("grenade", "o", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 4)
            self.listOfWeapons.append(w2)
        else:
            w1 = Weapon("gun", "/", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 7)
            self.listOfWeapons.append(w1)
            w2 = Weapon("grenade", "o", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 4)
            self.listOfWeapons.append(w2)

    def play(self):
        self.printInstructions()
        # This while loop is to prevent players and items from being stacked
        stack = True
        while stack == True:
            self.drawUpdatedGameBoard()
            for ppl in self.listOfPlayers:
                for items in self.listOfTreasures:
                    for weaPons in self.listOfWeapons:
                        if ppl.x == items.x and ppl.y == items.y or ppl.x == weaPons.x and ppl.y == weaPons.y or items.x == weaPons.x and items.y == weaPons.y:
                            stack = True
                        else:
                            stack = False
        # MAIN GAME LOOP to ask players what they want to do
        currentPlayerNum = 0
        while (len(self.listOfTreasures) >= 1):
            # get the player object for the player whose turn it is
            currentPlayer = self.listOfPlayers[currentPlayerNum];
            # ask the player what they would like to do
            if (type(currentPlayer) == AIPlayer):
                if currentPlayer.energy <= 2.5:
                    choice = "r"
                elif currentPlayer.energy > 2:
                    choice = "m"
                print("Player " + str(currentPlayer.gameBoardSymbol) +", do you want to (m)ove or (r)est? ", choice)
                sleep(2)
                self.processPlayerInput(currentPlayer,choice)
                sleep(2)
            else:
                if currentPlayer.strikerange > 0:
                    q = True
                    while q == True:                 
                        print("Player " + str(currentPlayer.gameBoardSymbol) +", do you want to (m)ove or (r)est or (a)ttack? ", end ="")
                        choice = input("")
                        if choice == "m" or choice == "r" or choice == "a":
                            self.processPlayerInput(currentPlayer, choice)
                            q = False
                        else:
                            print("Wrong Input")

                else:
                    z = True
                    while z == True:
                        print("Player " + str(currentPlayer.gameBoardSymbol) +", do you want to (m)ove or (r)est? ", end ="")
                        choice = input("")
                        if choice == "m" or choice == "r":
                            self.processPlayerInput(currentPlayer, choice)
                            z = False
                        else:
                            print("Wrong Input")
            # show the updated player information and game board
            sleep(.5)
            clear()
            self.printUpdatedPlayerInformation()
            self.drawUpdatedGameBoard()
            if len(self.listOfPlayers) == 1:
                break
            # update whose turn it is
            currentPlayerNum += 1
            if currentPlayerNum >= len(self.listOfPlayers):
                currentPlayerNum = 0
        # Determining the winner of the game
        total = 0
        for players in self.listOfPlayers:
            if players.getPoints() > total:
                total = players.getPoints()
                winner = players.gameBoardSymbol
                print("Player " + str(winner) + " wins!")
            # This is incase players didn't collect any points but eliminated all other players
            else:
                if len(self.listOfPlayers) == 1:
                    winner = players.gameBoardSymbol
                    print("Player " + str(winner) + " wins!")
        
    def processPlayerInput(self, plyr, action) :
        global ordX, ordY
        if action == "m":
            if (type(plyr) == Player):  # move
                s = True
                while s == True:
                    direction = input("Which direction (r, l, u, or d)? ")
                    if direction == "r" or direction == "l" or direction == "u" or direction == "d":
                        z = True
                        while z == True: 
                            distance = int(input("How Far? "))
                            if distance > 0:
                                plyr.move(direction, distance, self.gameBoardWidth, self.gameBoardHeight, plyr.x, plyr.y)
                                z = False
                                s = False
                            else:
                                print("Wrong Input!")
                    else:
                        print("Wrong Input!")
            # This is for just the AI Players algorithm
            elif (type(plyr) == AIPlayer):
                closestPlayer = math.sqrt((self.gameBoardWidth**2) + (self.gameBoardHeight**2))
                closestTreasure = math.sqrt((self.gameBoardWidth**2) + (self.gameBoardHeight**2))
                
                # AI Player compares whats closer: Player or treasure by calculating the magnitude of a vector
                for allplayers in self.listOfPlayers:
                    if allplayers.x != plyr.x and allplayers.y != plyr.y or allplayers.x == plyr.x and allplayers.y != plyr.y or allplayers.x != plyr.x and allplayers.y == plyr.y:
                        PordX = allplayers.x - plyr.x
                        PordY = allplayers.y - plyr.y
                        playersXY = math.sqrt((PordX**2) + (PordY**2))
                        if playersXY < closestPlayer:
                            closestPlayer = playersXY
                            closeP = PordX
                            closeP = PordX
                    PordX = closeP
                    PordX = closeP
                for tres in self.listOfTreasures:
                    if tres.x != plyr.x and tres.y != plyr.y or tres.x == plyr.x and tres.y != plyr.y or tres.x != plyr.x and tres.y == plyr.y:
                        TordX = tres.x - plyr.x
                        TordY = tres.y - plyr.y
                        tresureXY = math.sqrt((TordX**2) + (TordY**2))
                        #print(tres.name,"(",tres.x,",",tres.y,")", "Distance:",tresureXY)
                        if tresureXY < closestTreasure:
                            closestTreasure = tresureXY
                            shortX = TordX
                            shortY = TordY
                    TordX = shortX
                    TordY = shortY
                
                # AI Player deciding whether to attack Player or get Treasure by which is closer                
                # uses the coordinates from the closest item to determine what approach to take
                if closestPlayer < closestTreasure:
                    closestObject = closestPlayer
                    ordX = PordX
                    ordY = PordY
                elif closestPlayer >= closestTreasure:
                    if (closestPlayer - closestTreasure) <= 1:
                        closestObject = closestPlayer
                        ordX = PordX
                        ordY = PordY
                    else:    
                        closestObject = closestTreasure
                        ordX = TordX
                        ordY = TordY
                
                # AI Player deciding what direction and how far to move
                # uses the coordinates from above to determine what values to use
                if closestObject <= self.difficulty:
                    if abs(ordX) >= abs(ordY):
                        if ordX != 0:
                            if ordX < 0:
                                direction = "l"
                                distance = abs(ordX)
                            elif ordX > 0:
                                direction = "r"
                                distance = abs(ordX)
                    elif abs(ordY) > abs(ordX):
                        if ordY != 0:
                            if ordY < 0:
                                direction = "u"
                                distance = abs(ordY)
                            elif ordY > 0:
                                direction = "d"
                                distance = abs(ordY)
                    print("Which direction (r, l, u, or d)? ",direction)
                    print("How Far? ", distance)
                    # Uses the same player move method as regular players
                    plyr.move(direction,distance,self.gameBoardWidth,self.gameBoardHeight, plyr.x, plyr.y)
                
                # AI player will teleport if distance from other players is too far and will lose energy each time
                elif closestObject > self.difficulty:
                    plyr.x = rand.randrange(self.gameBoardWidth)
                    plyr.y = rand.randrange(self.gameBoardHeight)
                    plyr.energy = plyr.energy - 1
                    print("Player Teleported!")
                

            # check to see if player moved to the location of another game item
            for treasure in self.listOfTreasures:
                if plyr.x == treasure.x and plyr.y == treasure.y:
                    plyr.collectTreasure(treasure)
                    print("You collected",treasure.name,"worth",treasure.pointValue,"points!")
                    self.listOfTreasures.remove(treasure)  # remove the treasure from the list of available treasures
                    break
            
            # This prevents the AI Players from caputuring weapons
            if (type(plyr) == Player):
                for weapon in self.listOfWeapons:
                    if plyr.x == weapon.x and plyr.y == weapon.y:
                            print("You acquired the",weapon.name,end ="")
                            print("!")
                            plyr.collectWeapons(weapon)
                            self.listOfWeapons.remove(weapon)  # remove the treasure from the list of available treasures
                            break
            
            # This is for eliminating players
            for ply in self.listOfPlayers:
                if ply.x == plyr.x and ply.y == plyr.y:
                    if ply.gameBoardSymbol != plyr.gameBoardSymbol:
                        print("You eliminated player", ply.gameBoardSymbol, "from the game!")
                        self.listOfPlayers.remove(ply)
                        break
        
        # Different amounts of energy when resting for players vs. AI Players
        elif action == "r":
            if (type(plyr) == Player):
                plyr.energy += 4.0
            elif (type(plyr) == AIPlayer):
                plyr.energy += random.randint(3,5)
            
        # The attack action which allows only real players use weapons
        elif action == "a":
            for attack in self.listOfPlayers:
                # Uses the magnitude of a vector to determine whether players are within striking range
                if attack.x != plyr.x and attack.y == plyr.y or attack.x == plyr.x and attack.y != plyr.y or attack.x != plyr.x and attack.y != plyr.y:
                    coordx = attack.x - plyr.x
                    coordy = attack.y - plyr.y
                    magXY = math.sqrt((coordx**2) + (coordy**2))
                    if magXY <= plyr.strikerange:
                        print("You eliminated player", attack.gameBoardSymbol, "from the game!")
                        self.listOfPlayers.remove(attack)
            
        # For if a wrong input was entered              
        else :
            print("Sorry, that is not a valid choice")
    
    # Updates the players stats for points and energy
    def printUpdatedPlayerInformation(self):
        for p in self.listOfPlayers:
            print("Player " + p.gameBoardSymbol + " has " + str(p.getPoints()) + " points and has " + str(p.energy) + " energy")

    # Creation of the gameboard - Didn't make any changes here  
    def drawUpdatedGameBoard(self) : 
        clear()
        self.printInstructions()
        self.printUpdatedPlayerInformation()    
        # loop through each game board space and either print the gameboard symbol
        # for what is located there or print a dot to represent nothing is there
        for y in range(0,self.gameBoardHeight):
            for x in range(0,self.gameBoardWidth):
                symbolToPrint = "."
                for treasure in self.listOfTreasures:
                   if treasure.x == x and treasure.y == y:
                      symbolToPrint = treasure.gameBoardSymbol
                for player in self.listOfPlayers:
                   if player.x == x and player.y == y:
                      symbolToPrint = player.gameBoardSymbol
                for weapon in self.listOfWeapons:
                    if weapon.x == x and weapon.y == y:
                        symbolToPrint = weapon.gameBoardSymbol
                print(symbolToPrint,end="")
            print() # go to next row
        print()
            # Check to make sure players and items aren't stacked on top of one another           

    # Game Instructions - I didn't make any changes here   
    def printInstructions(self) :
        print("Players move around the game board collecting treasures worth points")
        print("The game ends when all treasures have been collected or only 1 player is left")
        print("Here are the point values of all of the treasures:")
        for treasure in self.listOfTreasures :
            print( "   " + treasure.name + "(" + treasure.gameBoardSymbol + ") " + str(treasure.pointValue) )
        print()
    
