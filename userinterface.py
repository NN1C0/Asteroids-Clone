import pygame
import pygame_gui
import pygame_gui.core.colour_gradient
import event_constants
from events import trigger_event_continue, trigger_event_quit, trigger_event_restart

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_STARTING_HEALTH

class UserInterface(pygame_gui.UIManager):
    def __init__(self) -> None:
        self.screen_center_x = SCREEN_WIDTH // 2
        self.screen_center_y = SCREEN_HEIGHT // 2
        
        self.gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score_label = pygame_gui.elements.UILabel(pygame.Rect(20, 20, 100, 20), text="Score: 0", manager=self.gui_manager, anchors={'left': 'left', 'top': 'top'})
        self.health_label = pygame_gui.elements.UILabel(pygame.Rect(-200, 20, 100, 20), text=f"Health: {PLAYER_STARTING_HEALTH}", manager=self.gui_manager, anchors={'right': 'right', 'top': 'top'})
        self.message_label = pygame_gui.elements.UITextBox("", pygame.Rect(200, 50, -1, -1), manager=self.gui_manager, visible=False)
        self.end_score_label = pygame_gui.elements.UILabel(pygame.Rect(self.screen_center_x - 20, self.screen_center_y - 100, 100, 20), text="", manager=self.gui_manager)
        
        self.trans_background = pygame_gui.elements.UIWindow(
            rect=pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT)),
            manager=self.gui_manager,
            window_display_title='',
            object_id='#overlay_window',
            visible=False
        )
        self.continue_button = pygame_gui.elements.UIButton(
            (self.screen_center_x, self.screen_center_y - 20),
            "Continue",
            self.gui_manager,
            visible=False,
            parent_element=self.trans_background
        )
        self.restart_button = pygame_gui.elements.UIButton(
            (self.screen_center_x, self.screen_center_y - 20),
            "Restart",
            self.gui_manager,
            visible=False,
            parent_element=self.trans_background
        )
        self.quit_button = pygame_gui.elements.UIButton(
            (self.screen_center_x, self.screen_center_y + 20),
            "Quit",
            self.gui_manager,
            visible=False
        )
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
        
    def show_message(self, text, time = 2, text_effect = pygame_gui.TEXT_EFFECT_SHAKE):
        self.message_label.set_text(text)
        self.message_label.set_position(pygame.Vector2((SCREEN_WIDTH - self.message_label.relative_rect.width) // 2, 50))
        self.message_label.show()
        self.message_label.set_active_effect(text_effect)
        pygame.time.set_timer(event_constants.MESSAGE_LABEL_HIDE, time * 1000, 1)
    
    def hide_message(self):
        self.message_label.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
        self.message_label.hide()
        
    def show_game_over_screen(self, score):
        self.trans_background.background_colour = pygame.Color(0, 0, 255, 128)
        self.trans_background.rebuild()
        self.end_score_label.set_text(f"End score: {score}")
        
        self.end_score_label.show()
        #self.trans_background.show()
        #self.restart_button.show()
        self.quit_button.show()
        
    def hide_game_over_screen(self):
        self.end_score_label.hide()
        #self.trans_background.hide()
        self.restart_button.hide()
        self.quit_button.hide()
        
    def reset(self):
        self.__init__()