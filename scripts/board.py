import pygame

import random as rd

FONT: str = "Fira Sans"
FONT_SIZE: int = 30

class Board:
    def __init__(self, game, size: int) -> None:
        self.game = game
        self.size: int = size
        self.rows: list[list[int]] = [[0 for i in range(self.size)] for ii in range(self.size)]
        
        self.font: pygame.font.Font = pygame.font.SysFont(FONT, FONT_SIZE, True)

    def render(self) -> None:
        text = self.font.render("Hello World!", True, (255, 255, 255))
        self.game.display.blit(text, (0, 0))
