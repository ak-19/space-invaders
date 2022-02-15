import pygame
from alien import Alien

from color import Color
from gametext import GameText
from player import Player

class Game:

    def __init__(self, display) -> None:
        self.display = display        
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_stats = GameText(display)

        self.run = True
        self.pause = False

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
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False                                               
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.shoot()

            self.update()

            self.draw()
                                    
            self.clock.tick(self.fps)
    
    #helper methods

    def setup_sprites(self):
        self.player_bullet_group = pygame.sprite.Group()
        self.alien_bullet_group = pygame.sprite.Group()
        self.player = Player(self.player_bullet_group)
        self.player_group = pygame.sprite.Group(self.player)
        self.alien_group = pygame.sprite.Group()

        for i in range(12):
            self.alien_group.add(Alien(64 * i, 100, 2, self.alien_bullet_group))          

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
    

                  