import pygame

import random as rd

FONT: str = "Fira Sans"
FONT_SIZE: int = 3

class Board:
    def __init__(self, game, size: int) -> None:
        self.game = game
        
        self.size: int = size
        self.board: list[list[int]] = [[0 for i in range(self.size)] for ii in range(self.size)]
        
        self.font: pygame.font.Font = pygame.font.SysFont(FONT, int(min(self.game.display.get_width() / self.size, self.game.display.get_height() / self.size) / FONT_SIZE), True)

        self.movement: tuple[bool] = [False for _ in range(4)]

        self.populate()

    def update(self) -> None:
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

    def populate(self) -> None:
        empty: list[list[int]] = []
        for i in range(self.size):
            for ii in range(self.size):
                if self.board[i][ii] == 0:
                    empty.append([i, ii])
        for _ in range(2):
            cell: list[int] = rd.choice(empty)
            self.board[cell[0]][cell[1]] = 4 if rd.randint(0, 100) <= 10 else 2
