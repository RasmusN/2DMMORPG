#!/usr/bin/python
"""
The Client main file
"""

import Creatures, pygame, time, Map
from c2s import ClientToServer
import __future__

FPS = 60
resolution = [800, 640]

visible_squares = 16 #
square_size = [resolution[0]/visible_squares, resolution[1]/visible_squares]

#Colors
white = (255,255,255)
black = (0,0,0)
red   = (255, 0, 0)
green = (0, 155, 0)

def main_menu():
    """Some kind of login"""
    connection = ClientToServer(ip = "192.168.1.1", 
                            port = "1234",
                            username = "Admin",
                            hns_password = "password")
        
    game_loop(connection)


def draw_background(gameDisplay, XY):
    """Draws the ground basically"""
    gameDisplay.fill(white)
    
def draw_gameDisplay(gameDisplay, hero):
    """Function writes graphics to GameDisplay"""
    
    draw_background(gameDisplay, [hero.x, hero.y])

    

def game_loop(connection):
    """The main loop"""    
    
    hero = Creatures.Human(name = "Hero", age = 33)
    
    #Set the window
    gameDisplay = pygame.display.set_mode(resolution)
    
    #Caption of the game
    pygame.display.set_caption('Troy')
    
    #Init the pygame clock
    clock = pygame.time.Clock()
    
    #Get back
    map = Map.Map(connection)
    
    #init eventlist
    eventlist = []
    
    game_exit = False
    
    while not game_exit:
        #do game here
        
        #Check if there is any ongoing events, update them
        for event in eventlist:
            pass
        
        #check for new events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
    
    
        draw_gameDisplay(gameDisplay, hero)

        #Update the display
        pygame.display.update()
                                
        #Tick
        clock.tick(FPS)
        

def main():
    """Main function"""
    #init pygame
    pygame.init()
    main_menu()
    
    
if __name__ == "__main__":
    main()