import pygame
from screen import Screen

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/invader.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass 

    #helper methods    
    def reset(self):
        pass

    def shoot(self):
        pass    
             
