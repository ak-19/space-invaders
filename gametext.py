import pygame

from color import Color

class GameText:
    def __init__(self, display) -> None:
        self.display = display
        self.main_font = pygame.font.Font('assets/font.ttf', 42)
        self.stats_font = pygame.font.Font('assets/font.ttf', 22)
        
    def draw_stats(self, score):
        score = self.stats_font.render(f'Score: {score}', True, Color.WHITE, Color.BLACK)
        score_rect = score.get_rect()
        score_rect.topleft = (10, 10)
        self.display.blit(score, score_rect)

