from randomNum import Random
rand= Random()
import math

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
        
    def move(self, direction, distanceToMove, boardWidth, boardHeight, posX, posY):
        # moving the players around the board and keeping players from going off the board
        if direction == "l":
            if distanceToMove <= (0 + posX): 
                self.x = self.x - self.enrgy(distanceToMove)           
            else:
                print("Too Far!")
        elif direction == "r":
            if distanceToMove < (boardWidth - posX):
                self.x = self.x + self.enrgy(distanceToMove)    
            else:
                print("Too Far!")
        elif direction == "u":
            if int(distanceToMove) <= (0 + posY):  
                self.y = self.y - self.enrgy(distanceToMove)
            else:
                print("Too Far!")           
        elif direction == "d":
            if distanceToMove < (boardHeight - posY):
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

# this is the AI class that inherets from the player classes attributes
class AIPlayer(Player):
    
    def __init__(self,initialX, initialY, symb):
        Player.__init__(self,initialX, initialY, symb)

# this method contains how AI players decide whether to attack other players or go after items
    def AImove(self,gameBoardWidth,gameBoardHeight,listOfPlayers,listOfTreasures,listOfWeapons,difficulty,plyr,):
                closestPlayer = math.sqrt((gameBoardWidth**2) + (gameBoardHeight**2))
                closestTreasure = math.sqrt((gameBoardWidth**2) + (gameBoardHeight**2))
                
                # AI Player compares whats closer: Player or treasure by calculating the magnitude of a vector
                for allplayers in listOfPlayers:
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
                for tres in listOfTreasures:
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
                    print("Which direction (r, l, u, or d)? ",direction)
                    print("How Far? ", distance)
                    # Uses the same player move method as regular players
                    plyr.move(direction,distance,gameBoardWidth,gameBoardHeight, plyr.x, plyr.y)
                
                # AI player will teleport if distance from other players is too far and will lose energy each time
                elif closestObject > difficulty:

                    self.teleport(gameBoardWidth,gameBoardHeight,plyr,listOfPlayers,listOfTreasures,listOfWeapons)

# This is the teleport method to allow AI player to move close with out stacking on top of any other player or item
    def teleport(self,gameBoardWidth,gameBoardHeight,plyr,listOfPlayers,listOfItems,listOfWeapons):
        e = True
        while e == True:
            plyr.x = rand.randrange(gameBoardWidth)
            plyr.y = rand.randrange(gameBoardHeight)
            for plrPos in listOfPlayers:
                if plrPos.x != plyr.x and plrPos.y != plyr.y:
                    for itmPos in listOfItems:
                        if itmPos.x != plyr.x and itmPos.y != plyr.y:
                            for WpPos in listOfWeapons:
                                if WpPos.x != plyr.x and WpPos.y != plyr.y:
                                    e = False
                                    break
        plyr.energy = plyr.energy - 1
        print("Player Teleported!")
