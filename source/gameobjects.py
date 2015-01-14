class GameObject(object)
    """All GameObjects should inherit from this function."""
    
    def __init__(self, x, y):
        """All objects are of 1x1 and have a position X, Y"""
        self.x = x
        self.y = y
