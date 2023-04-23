

class Weapon():
    def __init__(self, nm, symb, xCoord, yCoord, range):
        self.name =  nm
        self.gameBoardSymbol = symb # gameboard symbol
        self.x = xCoord # gameboard coordinates
        self.y = yCoord # gameboard coordinates
        self.strikerange = range # weapon strike range
        