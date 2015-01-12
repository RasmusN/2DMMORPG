#! /usr/bin/python

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
    
    def __init__(self, name, age = 0, x = 10, y = 10):
        self.__name = name
        self.__age = age
        
    def image(self):
        pass
        
 
    