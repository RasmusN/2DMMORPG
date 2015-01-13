#Length of the longest side of the map (square?)
LENGTH = 100

class Map(object):
    """Class handles the visual world
    
        The coordinates are defined in the same way as pixels are defined.
        X goes from left to right
        Y goes from top to bottom
    """
    
    #The world is 100x100 squares
    world = [[None for x in range(100)] for x in range(100)] 
    
    def __init__(self, connection):
        
        #Load map from harddrive
        self.__load_map()
        
        #Get near map from server
        connection.request_field_of_view()
        
    def __load_map(self):
        """Loads map from prev. sessions"""
        self.world =  [[1 for x in range(100)] for x in range(100)]
        
        #A small river
        self.world[14][14] = 3
        self.world[14][13] = 3
        self.world[14][12] = 3
        self.world[14][11] = 3
        self.world[14][10] = 3
    
        
Unknown = None
Grass   = 1
Sand    = 2
Water   = 3
Stone   = 4
Dirt    = 5