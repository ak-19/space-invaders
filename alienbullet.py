import pygame
from screen import Screen

class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/red-beem.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.bullet_group = bullet_group
        bullet_group.add(self)
        self.velocity = 10        

    def update(self):
        self.rect.y += self.velocity        
        if self.rect.bottom >= Screen.HEIGHT: self.kill()
    
             
