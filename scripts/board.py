import pygame

import random as rd

from scripts.utils import rotate90

FONT: str = "Fira Sans"
FONT_SCALE: int = 3

class Board:
    def __init__(self, game, size: int) -> None:
        self.game = game
        
        self.size: int = size
        self.board: list[list[int]] = [[0 for i in range(self.size)] for ii in range(self.size)]
        
        font_size: int = int(min(self.game.display.get_width() / self.size, self.game.display.get_height() / self.size) / FONT_SCALE)
        self.font: pygame.font.Font = pygame.font.SysFont(FONT, font_size, True)

        self.populate(2)

    def update(self, direction: int) -> None:
        new_board = rotate90(self.board, self.size, direction)

        for row in new_board:
            for cell in row:
                pass


    def render(self) -> None:
        divider: float = 2.5
        x: float = (self.game.display.get_width() / self.size) / divider
        y: float = (self.game.display.get_height() / self.size) / divider
        
        for row in self.board:
            for cell in row:
                text: pygame.surface.Surface = self.font.render(str(cell), True, (255, 255, 255))
                self.game.display.blit(text, (x, y))
                x += self.game.display.get_width() / self.size
            
            x = (self.game.display.get_width() / self.size) / divider
            y += self.game.display.get_height() / self.size

    def populate(self, amount: int = 1) -> None:
        empty: list[list[int]] = []
        for i in range(self.size):
            for ii in range(self.size):
                if self.board[i][ii] == 0:
                    empty.append([i, ii])
        if len(empty):
            for _ in range(amount):
                cell: list[int] = rd.choice(empty)
                self.board[cell[0]][cell[1]] = 4 if rd.randint(0, 100) <= 10 else 2
