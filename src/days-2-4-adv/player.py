from inventory import Inventory

class Player():
    def __init__(self, name, room, score=0):
        self.name = name
        self.room = room
        self.score = score
        Inventory.__init__(self, self.name)
    def changeRoom(self, direction):
        next_room = self.room.getRoomInDirection(direction)
        if next_room == None:
            print(f"\nLocation unchanged. There is nothing {direction}.")
        else: 
            self.room = next_room
            print(f'\nYou are currently: \n{self.room}')
    def lookRoom(self, direction):
        next_room = self.room.getRoomInDirection(direction)
        if next_room == None:
            print(f"\nThere is nothing {direction}.")
        else: 
            print(f'\nGoing {direction} will take you to: \n{next_room}')
    def playerItems(self):
        Inventory.showItems(self, self.name)
        self.getScore()
    def addItem(self, newItem):
        newPoints = Inventory.addItem(self, newItem)
        self.score = self.score + newPoints
        Inventory.removePoints(self, newItem)
        Inventory.showItems(self, self.name)
        self.getScore()
    def dropItem(self, newItem):
        Inventory.dropItem(self, newItem)
    def getScore(self):
        print(f"\n    Current Score: {self.score}")
    def getItem(self, name):
        return Inventory.getItem(self, name)