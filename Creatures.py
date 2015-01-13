#! /usr/bin/python
import Map

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
        if direction == "left":
            self.x -= 1
            self.direction = "left"
        elif direction == "right":
            self.x += 1
            self.direction = "right"
        elif direction == "up":
            self.y -= 1
            self.direction = "up"
        elif direction == "down":
            self.y += 1
            self.direction = "down"
            
class Human(Creature):
    __id = None
    __name = ""
        
    Map = None
    
    def __init__(self, connection, name, age = 0, x = 10, y = 10):
        self.__name = name
        self.__age = age

        self.x, self.y = x, y
        
        self.Map = Map.Map(connection)
        
    def image(self):
        pass
        
        
    