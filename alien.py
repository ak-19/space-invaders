import pygame
from random import randint

from alienbullet import AlienBullet
from screen import Screen

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, bullet_group) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/invader.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.start_pos = (x, y)

        self.velocity = velocity
        self.bullet_group = bullet_group

        self.direction = 1

        self.shoot_sound = pygame.mixer.Sound('assets/alien_fire.wav')
        self.shoot_sound.set_volume(.2)        


    def update(self):
        if self.rect.x + self.direction * self.velocity + 64 >= Screen.WIDTH or self.rect.x + self.direction * self.velocity < 0:
            self.direction *= - 1

        self.rect.x += self.direction * self.velocity 

        if randint(1, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot()


    #helper methods    
    def reset(self):
        self.rect.topleft = self.start_pos

    def shoot(self):
        self.shoot_sound.play()
        AlienBullet(self.rect.centerx, self.rect.centery ,self.bullet_group)
             
