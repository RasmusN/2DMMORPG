class Event(object):
    time_start = None
    time_end = None

    def __init__(self, t1, dt):
        """"""
        self.time_start = t1
        self.time_end = t1+dt
        
class EventMoveObject(Event):
    """This class handles movement of gameobjects"""
    object = None
    direction = None
    
    def __init__(self, game_object, direction, t1, dt):
        super(EventMoveObject, self).__init__(t1, dt)
        
        self.game_object = game_object
        self.direction = direction
        if direction == "up":
            self.new_position = [game_object.x, game_object.y - 1]
        elif direction == "down":
            self.new_position = [game_object.x, game_object.y + 1]
        elif direction == "left":
            self.new_position = [game_object.x - 1, game_object.y]
        elif direction == "right":
            self.new_position = [game_object.x + 1, game_object.y]
        
        
    def verify(game_state):
        """Verifies that it is actually posible to move
        self.object one step in self.direction"""
        if game_state.is_occupied(self.new_position):
            return False
        
        if 1: #Test other things, maby if it is within reach
            pass
        
        Return True
