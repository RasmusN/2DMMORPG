class GameState(object):
    """State of the game
    
    Both the server and the client has a instance of this class.
    
    The server knows everything. The client only knows what the hero knows.
    """
    
    #A list containing all known GameObjects in the world
    #This includes stones, wood, players, creatures
    game_objects = []

    def __init__(self)
        #Load saved state
        pass

    def add_object(self, object):
        game_objects.append(object)
        
    def is_occupied(self, xy):
        """Returns True if square is occupied by an object"""
        for object in game_objects:
            if [object.x, object.y] == xy:
                return True
    
