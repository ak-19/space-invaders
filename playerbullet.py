import pygame
from screen import Screen

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()

    def update(self):
        pass 
    
             
