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
if len(sys.argv) > 1:
  rand.setSeed(int(sys.argv[1]))

class Game:
    
    # the constructor (initialize all game variables)
    def __init__(self, width, height,numPlayers,AIplayers):  
        self.gameBoardWidth = width;
        self.gameBoardHeight = height;
        self.listOfPlayers = []
        self.listOfTreasures = []
        self.listOfWeapons = []
        p = 1
        for plyrs in range(numPlayers):
            positionx = rand.randrange(self.gameBoardWidth)
            positiony = rand.randrange(self.gameBoardHeight)
            player = Player(positionx,positiony,str(p))
            self.listOfPlayers.append(player)
            p += 1
        while (len(self.listOfPlayers) - 1) < AIplayers:
            positionx = rand.randrange(self.gameBoardWidth)
            positiony = rand.randrange(self.gameBoardHeight)            
            for position in self.listOfPlayers:
                if position.x == positionx and position.y == positiony:
                    positionx = rand.randrange(self.gameBoardWidth)
                    positiony = rand.randrange(self.gameBoardHeight)
                for pos in self.listOfTreasures:
                    if pos.x == positionx and pos.y == positiony:
                        positionx = rand.randrange(self.gameBoardWidth)
                        positiony = rand.randrange(self.gameBoardHeight)
                    for posT in self.listOfWeapons:
                        if posT == positionx and posT == positiony:
                            positionx = rand.randrange(self.gameBoardWidth)
                            positiony = rand.randrange(self.gameBoardHeight)
            player = AIPlayer(positionx,positiony,str(p))
            self.listOfPlayers.append(player)
            p += 1

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
        w1 = Weapon("gun", "/", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 7)
        self.listOfWeapons.append(w1)
        w2 = Weapon("grenade", "o", rand.randrange(self.gameBoardWidth),rand.randrange(self.gameBoardHeight), 4)
        self.listOfWeapons.append(w2)

    def play(self):
        self.printInstructions()
        self.drawUpdatedGameBoard()
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
                self.processPlayerInput(currentPlayer,choice)
            else:
                print("Player " + str(currentPlayer.gameBoardSymbol) +", do you want to (m)ove or (r)est? ", end ="")
                choice = input("")
                self.processPlayerInput(currentPlayer, choice)
            # show the updated player information and game board
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
            if len(self.listOfPlayers) == 1:
                winner = players.gameBoardSymbol
                print("Player " + str(winner) + " wins!")
            
    def processPlayerInput(self, plyr, action) :
        global ordX, ordY
        if action == "m":
            if (type(plyr) == Player):  # move
                direction = input("Which direction (r, l, u, or d)? ")
                distance = int(input("How Far? "))
                plyr.move(direction, distance, self.gameBoardWidth, self.gameBoardHeight, plyr.x, plyr.y)
            elif (type(plyr) == AIPlayer):
                closestPlayer = math.sqrt((self.gameBoardWidth**2) + (self.gameBoardHeight**2))
                closestTreasure = math.sqrt((self.gameBoardWidth**2) + (self.gameBoardHeight**2))
                
                # AI Player compares whats closer: Player or treasure
                
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
                
                # AI Player deciding whether to attack Player or get Treasure                
                
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
                
                if closestObject <= 6:
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
                    plyr.move(direction,distance,self.gameBoardWidth,self.gameBoardHeight, plyr.x, plyr.y)
                
                # AI player will teleport if distance from other players is too far
                
                elif closestObject > 6:
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
            if (type(plyr) == Player):
                for weapon in self.listOfWeapons:
                    if plyr.x == weapon.x and plyr.y == weapon.y:
                            print("You acquired the",weapon.name,end ="")
                            print("!")
                            plyr.collectWeapons(weapon)
                            self.listOfWeapons.remove(weapon)  # remove the treasure from the list of available treasures
                            print(plyr.strikerange)
                            break
            for ply in self.listOfPlayers:
                if ply.x == plyr.x and ply.y == plyr.y:
                    if ply.gameBoardSymbol != plyr.gameBoardSymbol:
                        print("You eliminated player", ply.gameBoardSymbol, "from the game!")
                        self.listOfPlayers.remove(ply)
                        break
        elif action == "r":
            if (type(plyr) == Player):
                plyr.energy += 4.0
            elif (type(plyr) == AIPlayer):
                plyr.energy += random.randint(3,5)
        elif action == "a":
            for attack in self.listOfPlayers:
                if attack.x != plyr.x and attack.y == plyr.y or attack.x == plyr.x and attack.y != plyr.y or attack.x != plyr.x and attack.y != plyr.y:
                    coordx = attack.x - plyr.x
                    coordy = attack.y - plyr.y
                    magXY = math.sqrt((coordx**2) + (coordy**2))
                    if magXY <= plyr.strikerange:
                        print("You eliminated player", attack.gameBoardSymbol, "from the game!")
                        self.listOfPlayers.remove(attack)
                       
        else :
            print("Sorry, that is not a valid choice")

    def printUpdatedPlayerInformation(self):
        for p in self.listOfPlayers:
            print("Player " + p.gameBoardSymbol + " has " + str(p.getPoints()) + " points and has " + str(p.energy) + " energy")
      
    def drawUpdatedGameBoard(self) :     
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
       
    def printInstructions(self) :
        print("Players move around the game board collecting treasures worth points")
        print("The game ends when all treasures have been collected or only 1 player is left")
        print("Here are the point values of all of the treasures:")
        for treasure in self.listOfTreasures :
            print( "   " + treasure.name + "(" + treasure.gameBoardSymbol + ") " + str(treasure.pointValue) )
        print()
    
