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

    def update(self) -> None:
        pass

    def render(self) -> None:
        x: float = (self.game.display.get_width() / self.size) / 1.5
        y: float = (self.game.display.get_height() / self.size) / 1.5
        for row in self.rows:
            for cel in row:
                text: pygame.surface.Surface = self.font.render(str(cel), True, (255, 255, 255))
                self.game.display.blit(text, (x, y))
                x += self.game.display.get_width() / self.size
            x = (self.game.display.get_width() / self.size) / 2
            y += self.game.display.get_height() / self.size
