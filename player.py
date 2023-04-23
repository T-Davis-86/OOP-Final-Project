from randomNum import Random


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
    
