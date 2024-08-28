import pygame

DESTROY_ASTEROID = pygame.event.custom_type()
UPDATE_HEALTHBAR = pygame.event.custom_type()

MESSAGE_LABEL_SHOW = pygame.event.custom_type()
MESSAGE_LABEL_HIDE = pygame.event.custom_type()

GAME_CONTINUE = pygame.event.custom_type()
GAME_PAUSE = pygame.event.custom_type()
GAME_RESTART = pygame.event.custom_type()
GAME_QUIT = pygame.event.custom_type()

PLAYER_VULNERABLE = pygame.event.custom_type()

PLAYER_DEAD = pygame.event.custom_type()