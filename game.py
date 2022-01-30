import pygame
from alien import Alien

from color import Color
from eventvalidator import EventValidator
from player import Player

class Game:

    def __init__(self, display) -> None:
        self.display = display        
        self.event_validation = EventValidator()
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.player_group = pygame.sprite.Group()
        self.player_group.add(Player())

        self.alien_group = pygame.sprite.Group()

        for i in range(12):
            self.alien_group.add(Alien(64 * i,100))


    def update(self):
        self.player_group.update()
        self.alien_group.update()
        pass

    def draw(self):
        self.display.fill(Color.BLACK)
                    
        self.player_group.draw(self.display)
        self.alien_group.draw(self.display)

        pygame.display.update()

    def run_game_loop(self):
        while self.event_validation.ok():

            self.update()

            self.draw()
                                    
            self.clock.tick(self.fps)
    

    #helper methods

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
    

                  