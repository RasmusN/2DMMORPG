
class ClientToServer(object):
    """This class handles the communication
    to the server"""
    
    __logged_in = False
    __username = ""
    
    def __init__(self, ip, port, username, hns_password):
        """
        Connect to server
        """
        self.username = username
        pass
    
    def login(username, hns_password):
        """Request to login"""
        __logged_in = True
    
    def move(self, creature, direction):
        """Ask the server for permission to move"""
        return True
    
    def request_field_of_view(self):
        """Returns the fields nearest to the player"""
        return None