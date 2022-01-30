import pygame
from alien import Alien

from color import Color
from eventvalidator import EventValidator
from gametext import GameText
from player import Player

class Game:

    def __init__(self, display) -> None:
        self.display = display        
        self.event_validation = EventValidator()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_stats = GameText(display)

        self.setup_sprites()
  
    def update(self):
        self.player_bullet_group.update()
        self.alien_bullet_group.update()
        self.player_group.update()
        self.alien_group.update()

    def draw(self):
        self.display.fill(Color.BLACK)

        self.game_stats.draw_stats(123)
                    
        self.player_bullet_group.draw(self.display)
        self.alien_bullet_group.draw(self.display)
        self.player_group.draw(self.display)
        self.alien_group.draw(self.display)

        pygame.display.update()

    def run_game_loop(self):
        while self.event_validation.ok():

            self.update()

            self.draw()
                                    
            self.clock.tick(self.fps)
    
    #helper methods

    def setup_sprites(self):
        self.player_bullet_group = pygame.sprite.Group()
        self.alien_bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group(Player(self.player_bullet_group))
        self.alien_group = pygame.sprite.Group()

        for i in range(12):
            self.alien_group.add(Alien(64 * i,100))          

    def draw_game_stats(self):
        pass

    def check_collisions(self):
        pass

    def shift_aliens(self):
        pass    

    def start_new_round(self):
        pass

    def check_round_completion(self):
        pass

    def check_game_status(self):
        pass

    def pause_game(self):
        pass

    def reset_game(self):
        pass
    

                  