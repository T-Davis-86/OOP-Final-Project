class Treasure :

    # constructor (initialilze all variables for a treasure)
    def __init__(self, nm, symb, pointVal, xCoord, yCoord) :
        self.name = nm
        self.gameBoardSymbol = symb # gameboard symbol
        self.pointValue = pointVal # goint value for each item
        self.x = xCoord # gameboard coordinates
        self.y = yCoord # gameboard coordinates

