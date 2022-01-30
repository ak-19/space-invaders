import pygame
from screen import Screen

class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = Screen.WIDTH // 2
        self.rect.bottom = Screen.HEIGHT

        self.bullet_group = bullet_group

        self.lives = 5
        self.velocity = 8

        self.shoot_sound = pygame.mixer.Sound('assets/player_fire.wav')
        self.shoot_sound.set_volume(.2)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.velocity
        elif pressed_keys[pygame.K_RIGHT] and self.rect.right <= Screen.WIDTH:
            self.rect.x += self.velocity

        if pressed_keys[pygame.K_SPACE]:
            self.shoot()

    #helper methods    
    def reset(self):
        pass

    def shoot(self):
        self.shoot_sound.play()
             
