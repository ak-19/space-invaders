import pygame
from screen import Screen

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = Screen.WIDTH // 2
        self.rect.y = Screen.HEIGHT - 80

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 10
        elif pressed_keys[pygame.K_RIGHT] and self.rect.right <= Screen.WIDTH:
            self.rect.x += 10   

    #helper methods    
    def reset(self):
        pass

    def shoot(self):
        pass    
             
