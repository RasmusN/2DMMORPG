#!/usr/bin/python
"""
The Client main file
"""

import Creatures, pygame, time, Map
from c2s import ClientToServer
import __future__

FPS = 15
resolution = [800, 640]

visible_squares = [17, 17] #

#XY square_size
square_size = [int(resolution[0]/visible_squares[0]),
               int(resolution[1]/visible_squares[1])]
            
print "Resolution", resolution
print "Square size", square_size, "pxl/sqare"

#Colors
white = (255,255,255)
black = (  0,  0,  0)
red   = (255,  0,  0)
green = (0,  155,  0)
blue  = (0,    0,255)
bech  = (255,204, 51)

def g2l(global_x, global_y, hero):
    """Converts to global xy-coordinates to local coordinates relative
    to hero. 
    
    Note that this function does not care if the local coordinates is
    actually visible. It's the the relative coordinates"""
    
    l_hero_x = (visible_squares[0]-1)/2 #8
    l_hero_y = (visible_squares[1]-1)/2 #8
    
    
    local_x = global_x - hero.x + l_hero_x
    local_y = global_y - hero.y + l_hero_y
    
    return local_x, local_y
    
def l2g(local_x, local_y, hero):
    """
    Converts to local xy-coordinates to global coordinates relative
    to hero.
    """
    l_hero_x = (visible_squares[0]-1)/2 #8
    l_hero_y = (visible_squares[1]-1)/2 #8
    
    global_x = local_x + hero.x - l_hero_x
    global_y = local_y + hero.y - l_hero_y   

    #global_x = hero.x + x
    #global_y = hero.y + y
    
    return global_x, global_y
    
def l2p(x, y):
    """Takes the game coordinates and returns the 
    corresponding value of the upper left pixel coordinate on the screen"""
    
    return square_size[0]*x, square_size[1]*y
    
def main_menu():
    """Some kind of login"""
    connection = ClientToServer(ip = "192.168.1.1", 
                            port = "1234",
                            username = "Admin",
                            hns_password = "password")
        
    game_loop(connection)


def draw_field_of_view(gameDisplay, hero):
    """Draws the ground basically"""
    #Fill with black
    gameDisplay.fill(white)
    
    #Draw ground
    
    for x in range(visible_squares[0]):
        #From left to right <-> 0 to 16
        #
        for y in range(visible_squares[1]):
            g_x, g_y = l2g(x, y, hero)
            p_x, p_y = l2p(x, y)
            
            if not hero.Map.world[g_x][g_y]:
                """This should only be the case if the player
                is within sight of the edge of earth"""
                pygame.draw.rect(gameDisplay, 
                                black, 
                                [p_x, p_y,square_size[0], square_size[1]]
                                )
                
            elif hero.Map.world[g_x][g_y] == 1:
                pygame.draw.rect(gameDisplay, green, 
                                [p_x, p_y,square_size[0], square_size[1]])

            elif hero.Map.world[g_x][g_y] == 2:
                pygame.draw.rect(gameDisplay, bech, 
                                [p_x, p_y, square_size[0], square_size[1]])
                                
            elif hero.Map.world[g_x][g_y] == 3:
                pygame.draw.rect(gameDisplay, blue, 
                                [p_x, p_y, square_size[0], square_size[1]])
                
        
    #pygame.draw.rect(gameDisplay, red, [px, py, square_size, square_size])    

    #draw_hero
    hero_px, hero_py = l2p(8, 8)
            
    pygame.draw.rect(gameDisplay, red, [hero_px, hero_py, 
                    square_size[0], square_size[1]])
    #gameDisplay.draw
    
def draw_gameDisplay(gameDisplay, hero):
    """Function writes graphics to GameDisplay"""
    
    draw_background(gameDisplay, hero)

    
def game_loop(connection):
    """The main loop"""    
    
    hero = Creatures.Human(connection, name = "Hero", age = 33)
    
    #Set the window
    gameDisplay = pygame.display.set_mode(resolution)
    
    #Caption of the game
    pygame.display.set_caption('Troy')
    
    #Init the pygame clock
    clock = pygame.time.Clock()

    
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
    
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.move("left")
                    
                if event.key == pygame.K_RIGHT:
                    hero.move("right")
                    
                if event.key == pygame.K_UP:
                    hero.move("up")
                    
                if event.key == pygame.K_DOWN:
                    hero.move("down")
    
        draw_field_of_view(gameDisplay, hero)

        #Update the display
        pygame.display.update()
                                
        #Tick
        clock.tick(FPS)
        
        #print "Hero position: ", hero.x, hero.y
        

def main():
    """Main function"""
    #init pygame
    pygame.init()
    main_menu()
    
    
if __name__ == "__main__":
    main()
