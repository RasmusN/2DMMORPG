#! /usr/bin/python
import Map

class Creature(object):
    """All living things should inherit from this class"""
    __state = "alive"
    __age = None
    #__position = []
    x = 0
    y = 0
    
    def __init__(self, connection):
        pass    
    
    def move(self, direction):
        """"""
        pass
    
    
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
        
        
    