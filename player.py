from randomNum import Random
rand= Random()
import math
import random
from time import sleep

class Player :
    # the constructor (initialize all Player variables)
    def __init__(self, initialX, initialY, symb) :     
        self.x = initialX
        self.y = initialY
        self.energy = 8
        self.strikerange = 0 # strike range for weapons
        self.collectedTreasures = [] # list that contains all treasures collected by players
        self.collectedWeapons = [] # List that contains weapons collected by players
        self.gameBoardSymbol = symb
        
    # used to calculate points in the game for each player   
    def getPoints(self):
        totalPoints = 0
        for i in self.collectedTreasures:
            totalPoints += i
        return totalPoints
    # used after landing on an object and adding that to players inventory  
    def collectTreasure(self, treasureItem) :
        self.collectedTreasures.append(treasureItem.pointValue)
    
    # used after landing on a weapon and adding it to players inventory
    def collectWeapons(self,Weapon):
        self.collectedWeapons.append(Weapon)
        # If multiple weapons are gather by single player
        # This determines which has a longer strike range and uses it
        longest = 0
        for distant in self.collectedWeapons:
            if distant.strikerange > longest:
                longest = distant.strikerange
                self.strikerange = longest
        
    def move(self, direction, distanceToMove, boardWidth, boardHeight, listOfPlayers,listOfTreasures,difficulty,Weapons):
        # moving the players around the board and keeping players from going off the board
        if direction == "l":
            if distanceToMove <= (0 + self.x): 
                self.x = self.x - self.enrgy(distanceToMove)           
            else:
                print("Too Far!")
        elif direction == "r":
            if distanceToMove < (boardWidth - self.x):
                self.x = self.x + self.enrgy(distanceToMove)    
            else:
                print("Too Far!")
        elif direction == "u":
            if int(distanceToMove) <= (0 + self.y):  
                self.y = self.y - self.enrgy(distanceToMove)
            else:
                print("Too Far!")           
        elif direction == "d":
            if distanceToMove < (boardHeight - self.y):
                self.y = self.y + self.enrgy(distanceToMove)
            else:
                print("Too Far!")  
        # For if a user inputs wrong key for direction
        else:
            print("That is not a valid direction")
    
    # used to calculate the amount of energy depleted for each move
    def enrgy(self,distance):
        value = 0
        for dist in range(distance):
            if self.energy > 0:
                self.energy = self.energy - .5     
            elif self.energy <= 0:
                return value
            value += 1
        return value
    
    # rest method and determines how much energy is gained upon a rest by plyer type
    def rest(self):
        self.energy += 4.0
        
            

# this is the AI class that inherets from the player classes attributes
class AIPlayer(Player):
    
    def __init__(self,initialX, initialY, symb):
        Player.__init__(self,initialX, initialY, symb)

# this method contains how AI players decide whether to attack other players or go after items
    def move(self,direction, distance, gameBoardWidth, gameBoardHeight, listOfPlayers, listOfTreasures, difficulty, listOfWeapons):
                closestPlayer = math.sqrt((gameBoardWidth**2) + (gameBoardHeight**2))
                closestTreasure = math.sqrt((gameBoardWidth**2) + (gameBoardHeight**2))
                
                # AI Player compares whats closer: Player or treasure by calculating the magnitude of a vector
                for allplayers in listOfPlayers:
                    if allplayers.x != self.x and allplayers.y != self.y or allplayers.x == self.x and allplayers.y != self.y or allplayers.x != self.x and allplayers.y == self.y:
                        PordX = allplayers.x - self.x
                        PordY = allplayers.y - self.y
                        playersXY = math.sqrt((PordX**2) + (PordY**2))
                        if playersXY < closestPlayer:
                            closestPlayer = playersXY
                            closePx = PordX
                            closePy = PordY
                for tres in listOfTreasures:
                    if tres.x != self.x and tres.y != self.y or tres.x == self.x and tres.y != self.y or tres.x != self.x and tres.y == self.y:
                        TordX = tres.x - self.x
                        TordY = tres.y - self.y
                        tresureXY = math.sqrt((TordX**2) + (TordY**2))
                        if tresureXY < closestTreasure:
                            closestTreasure = tresureXY
                            closeTx = TordX
                            closeTy = TordY
                # AI Player deciding whether to attack Player or get Treasure by which is closer                
                # uses the coordinates from the closest item to determine what approach to take
                if closestPlayer < closestTreasure:
                    closestObject = closestPlayer
                    ordX = closePx
                    ordY = closePy
                elif closestPlayer >= closestTreasure:
                    if (closestPlayer - closestTreasure) <= 1:
                        closestObject = closestPlayer
                        ordX = closePx
                        ordY = closePy
                    else:    
                        closestObject = closestTreasure
                        ordX = closeTx
                        ordY = closeTy
                
                # AI Player deciding what direction and how far to move
                # uses the coordinates from above to determine what values to use
                if closestObject <= difficulty:
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
                    print("Which direction (r, l, u, or d)? ",end= "")
                    sleep(1)
                    print(direction)
                    print("How Far? ", end="")
                    sleep(1)
                    print(distance)
                    # Uses the same player move method as regular players
                    Player.move(self,direction, distance, gameBoardWidth, gameBoardHeight, listOfPlayers, listOfTreasures, difficulty, listOfWeapons)
                
                # AI player will teleport if distance from other players is too far and will lose energy each time
                elif closestObject > difficulty:
                    self.teleport(gameBoardWidth,gameBoardHeight,listOfPlayers,listOfTreasures, listOfWeapons)

# This is the teleport method to allow AI player to move close with out stacking on top of any other player or item
    def teleport(self,gameBoardWidth,gameBoardHeight,listOfPlayers,listOfItems,listOfWeapons):
        tele = True
        print(len(listOfPlayers))
        while tele == True:
            tele1 = 0
            tele2 = 0
            tele3 = 0
            tele4 = 0
            tele5 = 1
            self.x = random.randint(0,gameBoardWidth)
            self.y = random.randint(0,gameBoardHeight)
            print(self.x,self.y,self.gameBoardSymbol)
            for items in listOfItems:
                #print(items.x,items.y,items.gameBoardSymbol)
                if self.x != items.x and self.x != items.y or self.x != items.x and self.y == items.y or self.x == items.x and self.y != items.y:
                    tele1 += 1
                    if tele1 == len(listOfItems):                          
                        for wpons in listOfWeapons:
                            #print(wpons.x,wpons.y,wpons.gameBoardSymbol)
                            if self.x != wpons.x and self.y != wpons.y or self.x != wpons.x and self.y == wpons.y or self.x == wpons.x and self.y != wpons.y:
                                tele2 += 1
                                if tele2 == len(listOfWeapons):     
                                    for players in listOfPlayers:
                                        #print(players.x,players.y,players.gameBoardSymbol)
                                        if self.x == players.x and self.y == players.y and self.gameBoardSymbol == players.gameBoardSymbol or self.x == players.x and self.y != players.y or self.x != players.x and self.y == players.y:
                                            tele3 += 1
                                            tele4 += 1
                                            #print(tele3,tele4)
                                            if tele3 == len(listOfPlayers) and tele4 == tele5:
                                                tele = False
                                        else:
                                            tele3 += 1        


        self.energy = self.energy - 1
        print("Player Teleported!")

    
    def rest(self):
        self.energy += random.randint(3,5)