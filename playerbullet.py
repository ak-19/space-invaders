import pygame
from screen import Screen

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/green-beem.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        bullet_group.add(self)
        self.velocity = 10

    def update(self):
        self.rect.y -= self.velocity
    
             
