#! /usr/bin/python
import Map, troy

class Creature(object):
    """All living things should inherit from this class"""
    __state = "alive"
    __age = None
    #__position = []
    x = 0
    y = 0
    direction = "up"
    
    def __init__(self, connection):
        pass    
    
    def move(self, direction):
        """"""
        x = self.x
        y = self.y
        if direction == "left":
            if not self.Map.world[x-1][y] == 3:
                #print "Hero is moving left to: [%d,%d]" % x-1, x-1, y, self.Map.world[x-1][y]
                self.x -= 1
                self.direction = "left"
        elif direction == "right":
            if not self.Map.world[x+1][y] == 3:
                self.x += 1
                self.direction = "right"
        elif direction == "up":
            if not self.Map.world[x][y-1] == 3:
                self.y -= 1
                self.direction = "up"
        elif direction == "down":
            if not self.Map.world[x][y+1] == 3:
                self.y += 1
                self.direction = "down"
                
        lx , ly = troy.g2l(self.x, self.y, self)
        print "Hero: G(%d, %d) L(%d, %d)" % (self.x, self.y, lx, ly)
class Human(Creature):
    __id = None
    __name = ""
    
    def __init__(self, connection, name, age = 0, x = 10, y = 10):
        self.__name = name
        self.__age = age

        self.x, self.y = x, y
        
        self.Map = Map.Map(connection)
        
    def image(self):
        pass
        
        
    