#! /usr/bin/python

import events, controller
import Creatures
import pygame


class GameClass(object):
    """This is a 2D MMORPG"""
    
    #A list of visible objects
    visible_objects = []
    
    def __init__(self):
        #Create an observer
        self.observer = Observer()
        #event_handler = 
        self.gamestate = GameState()
        
        done = False

    def game_loop(self)
        """The Game Loop"""
        while not done:
            #Do game here
            
            #Get new events from server
            self.eventhandler.get_events_from_c2s()
            
            #Get evens from controller
            new_events = self.controller.get_new_events()
            failed_events = self.verify_events(new_events)
                    
            #Remove all failed events
            for event in failed_events:
                new_events.remove(event)
                
            
    def verify_events(self, event_list):
        """This method verifies all events in event_list"""


        #A list containing all failed events
        failed_events = []
        
        for event in eventlist:
            if not event.verify(GameState)
                failed_events.append(event)
            
if __names__ == "__main__":
    GameClass()
