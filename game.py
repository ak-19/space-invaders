import pygame

from color import Color
from eventvalidator import EventValidator
from spaceship import Spaceship

class Game:

    def __init__(self, display) -> None:
        self.display = display        
        self.event_validation = EventValidator()
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.spacehip_group = pygame.sprite.Group()
        self.spacehip_group.add(Spaceship())

    def update(self):
        self.spacehip_group.update()
        pass

    def draw(self):
        self.display.fill(Color.BLACK)
                    
        self.spacehip_group.draw(self.display)
        pygame.display.update()

    def run_game_loop(self):
        while self.event_validation.ok():

            self.update()

            self.draw()
                                    
            self.clock.tick(self.fps)
            

                  