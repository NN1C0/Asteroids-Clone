from typing import (
    Dict,
    Any,
)
import pygame
import event_constants


def trigger_custom_event(event_type, attr: Dict[str, Any] = None):
    if attr:
        return pygame.event.post(pygame.Event(event_type, attr))
    return pygame.event.post(pygame.Event(event_type))

def trigger_event_continue():
    trigger_custom_event(event_constants.GAME_CONTINUE)
    
def trigger_event_pause():
    trigger_custom_event(event_constants.GAME_PAUSE)
    
def trigger_event_restart():
    trigger_custom_event(event_constants.GAME_RESTART)
    
def trigger_event_quit():
    trigger_custom_event(event_constants.GAME_QUIT)