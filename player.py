import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_STARTING_HEALTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
    )
import event_constants
from events import trigger_custom_event

class Player(CircleShape):
    def __init__(self, x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.timer = 0
        self.color = "white"
        
        self.health = PLAYER_STARTING_HEALTH
        self.is_invincible = False
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.is_invincible:
            self.color = "red"
        else:
            self.color = "white"
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    def receive_damage(self, amount):
        if not self.is_invincible:
            self.is_invincible = True
            self.health -= amount
            trigger_custom_event(event_constants.UPDATE_HEALTHBAR, {"new_health": self.health})
            pygame.time.set_timer(pygame.Event(event_constants.PLAYER_VULNERABLE), 1500, 1)
            trigger_custom_event(event_constants.MESSAGE_LABEL_SHOW, {"message_text": "We have been hit!"})
            if self.health <= 0:
                trigger_custom_event(event_constants.PLAYER_DEAD)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(dt * (-1))
        if keys[pygame.K_s]:
            self.move(-(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def reset(self):
        self.__init__()