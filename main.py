import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from userinterface import UserInterface
from shot import Shot
import event_constants

def main():
    print("Starting asteroids!")
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    ui = UserInterface()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == event_constants.DESTROY_ASTEROID:
                ui.addKillToScore()
        
        screen.fill((0,0,0))
        ui.update(dt)
        ui.draw(screen)
        
        for u in updateable:
            u.update(dt)
            
        # Check for asteroid collisons
        for a in asteroids:
            if player.has_collided(a):
                print("Game over!")
                sys.exit()
            
            for s in shots:
                if s.has_collided(a):
                    a.split()
            
        for d in drawable: 
            d.draw(screen)      
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()