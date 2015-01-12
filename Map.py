
class Map(object):
    """Class handles the visual world"""
    
    #The world is 100x100 squares
    the_world = [[None for x in range(100)] for x in range(100)] 
    
    def __init__(self, connection):
        
        #Load map from harddrive
        self.__load_map()
        
        #Get near map from server
        connection.request_field_of_view()
        
    def __load_map(self):
        """Loads map from prev. sessions"""
        self.the_world =  [[2 for x in range(100)] for x in range(100)]
        
    
        
Unknown = None
Grass   = 1
Sand    = 2
Water   = 3
Stone   = 4
Dirt    = 5