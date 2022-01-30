import pygame

from screen import Screen

class Setup:
    def __init__(self) -> None:
        pygame.init()

    def get_display(self):
        return pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def quit(self) -> None:
        pygame.quit()        
    
