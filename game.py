import pygame
from alien import Alien

from color import Color
from gametext import GameText
from player import Player
from screen import Screen

class Game:

    def __init__(self, display) -> None:
        self.display = display        
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.game_stats = GameText(display)

        self.run = True

        self.new_round_sound = pygame.mixer.Sound('assets/new_round.wav')
        self.breach_sound = pygame.mixer.Sound('assets/breach.wav')
        self.alien_hit_sound = pygame.mixer.Sound('assets/alien_hit.wav')
        self.alien_hit_sound.set_volume(0.1)
        self.player_hit_sound = pygame.mixer.Sound('assets/player_hit.wav')
        
        self.setup_game()
  
    def setup_game(self):
        self.round_number = 1
        self.score = 0
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
        self.draw_game_stats()                    
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

        self.start_new_round()

    def draw_game_stats(self):
        self.game_stats.draw_stats(self.score, self.round_number, self.player.lives)

    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100

        player_hit = pygame.sprite.groupcollide(self.alien_bullet_group, self.player_group, True, False)
        
        if player_hit:
            self.player_hit_sound.play()
            self.player.lives -= len(player_hit)

            self.check_game_status()

    def shift_aliens(self):
        pass    
        #determine if invaders hit the edge
        shift = False
        for alien in self.alien_group:
            if alien.rect.left <= 0 or alien.rect.right >= Screen.WIDTH:
                shift = True

        if shift:
            breach = False
            for alien in self.alien_group.sprites():
                alien.direction *=  -1
                alien.rect.y += self.round_number * 10
                alien.rect.x += alien.velocity * alien.direction
                if alien.rect.bottom > Screen.HEIGHT - 100:
                    breach = True
            
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status()
        
    def start_new_round(self):
        for i in range(11):
            for j in range(5):
                self.alien_group.add(Alien(64 + 64 * i, 64 + 64 * j, 1, self.alien_bullet_group))       

        self.new_round_sound.play()
        self.pause_game('Start new round', 'press enter to start')

    def check_round_completion(self):
        if len(self.alien_group) == 0:
            self.score += 1000 * self.round_number
            self.round_number += 1
            self.start_new_round()

    def check_game_status(self):
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()

        self.player.reset()
        for alien in self.alien_group.sprites(): alien.reset()
        
        if self.player.lives == 0:
            self.reset_game(f'final score {self.score}', 'Press "enter" to play')
        else:
            self.pause_game('Lost life', 'press enter to start over')

    def pause_game(self, main_text, sub_text = ''):
        self.game_stats.draw_main_text(main_text, sub_text)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    paused = False   
                if event.type == pygame.QUIT:
                    paused = False
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = False
                    self.run = False                                                     

    def reset_game(self, text = '', sub_text = ''):
        self.game_stats.draw_main_text(text, sub_text)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.setup_game() 
                    paused = False
                elif event.type == pygame.QUIT:
                    paused = False
                    self.run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = False
                    self.run = False
    

                  