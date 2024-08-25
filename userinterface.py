import pygame
import pygame_gui

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class UserInterface(pygame_gui.UIManager):
    def __init__(self) -> None:
        self.gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score_label = pygame_gui.elements.UILabel(pygame.Rect(20, 20, 100, 20), text="Score: 0", manager=self.gui_manager, anchors={'left': 'left', 'top': 'top'})
        self.health_label = pygame_gui.elements.UILabel(pygame.Rect(-200, 20, 100, 20), text="Health: 100", manager=self.gui_manager, anchors={'right': 'right', 'top': 'top'})
        self.message_label = pygame_gui.elements.UITextBox("", pygame.Rect(200, 200, -1, -1), manager=self.gui_manager, visible=False)
        
        self.score = 0
        self.health = 0
    def draw(self, screen):
        self.gui_manager.draw_ui(screen)
        
    def update(self, dt):
        self.gui_manager.update(dt)
        
    def add_kill_to_score(self):
        self.score += 10
        self.score_label.set_text(f"Score: {int(self.score)}")
        
    def update_health_bar(self, new_health):
        self.health = new_health
        self.health_label.set_text(f"Health: {int(self.health)}")