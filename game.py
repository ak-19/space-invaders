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

        self.round_number = 1
        self.score = 0


        self.new_round_sound = pygame.mixer.Sound('assets/new_round.wav')
        self.breach_sound = pygame.mixer.Sound('assets/breach.wav')
        self.alien_hit_sound = pygame.mixer.Sound('assets/alien_hit.wav')
        self.player_hit_sound = pygame.mixer.Sound('assets/player_hit.wav')
        

        self.setup_sprites()
  
    def update(self):
        self.player_bullet_group.update()
        self.alien_bullet_group.update()
        self.player_group.update()
        self.alien_group.update()

        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self):
        self.display.fill(Color.BLACK)

        self.game_stats.draw_stats(self.score)
                    
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
            self.alien_group.add(Alien(64 * i, 100, 1, self.alien_bullet_group))          

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
    

                  