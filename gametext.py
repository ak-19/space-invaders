import pygame

from color import Color
from screen import Screen

class GameText:
    def __init__(self, display) -> None:
        self.display = display
        self.main_font = pygame.font.Font('assets/font.ttf', 42)
        self.stats_font = pygame.font.Font('assets/font.ttf', 22)

    def draw_main_text(self, text, sub_text):

        self.display.fill(Color.BLACK)

        main_text = self.main_font.render(text, True, Color.WHITE, Color.BLACK)
        main_text_rect = main_text.get_rect()

        s_text = self.stats_font.render(sub_text, True, Color.WHITE, Color.BLACK)
        s_rect = s_text.get_rect()


        s_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2 + 60)    
        main_text_rect.center = (Screen.WIDTH // 2, Screen.HEIGHT // 2)    

        self.display.blit(s_text, s_rect)
        self.display.blit(main_text, main_text_rect)

        pygame.display.update()
        
    def draw_stats(self, score, round, lives):
        score = self.stats_font.render(f'Score: {score}', True, Color.WHITE, Color.BLACK)
        score_rect = score.get_rect()
        score_rect.topleft = (10, 10)

        round = self.stats_font.render(f'Round: {round}', True, Color.WHITE, Color.BLACK)
        round_rect = round.get_rect()
        round_rect.centerx = Screen.WIDTH // 2
        round_rect.y = 10

        lives = self.stats_font.render(f'Lives: {lives}', True, Color.WHITE, Color.BLACK)
        lives_rect = lives.get_rect()
        lives_rect.right = Screen.WIDTH - 10
        lives_rect.y = 10

        self.display.blit(score, score_rect)
        self.display.blit(round, round_rect)
        self.display.blit(lives, lives_rect)

        pygame.draw.line(self.display, Color.WHITE, (0, 50), (Screen.WIDTH, 50), width = 1)
        pygame.draw.line(self.display, Color.WHITE, (0, Screen.HEIGHT - 100), (Screen.WIDTH, Screen.HEIGHT - 100), width = 1)

