import sys
import pygame

from scripts.board import Board

SCREEN_WIDTH: int = 500
SCREEN_HEIGHT: int = 500
SCREEN_SIZE: tuple[int] = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS_MAX: int = 60
WINDOW_TITLE: str = "2048"

BG_CLR: tuple[int] = (46, 52, 64)

BOARD_SIZE: int = 4

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        
        self.running: bool = True

        self.screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
        self.display: pygame.Surface = pygame.Surface(SCREEN_SIZE)
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.board: Board = Board(self, BOARD_SIZE)

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE: self.running = False
                    case pygame.QUIT: self.running = False

            self.display.fill(BG_CLR)

            self.board.render()

            self.screen.blit(self.display, (0, 0))

            pygame.display.update()

            self.clock.tick(FPS_MAX)

        pygame.quit()
        sys.exit(0)


def main() -> None:
    Game().run()

if __name__ == "__main__":
    main()
