import pygame

class EventValidator:
    def __init__(self) -> None:
        self.run = True
        self.pause = False

    def ok(self) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.run = False          
        return self.run