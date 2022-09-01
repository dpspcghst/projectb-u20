from sys import exit
import pygame
from level import Level
from settings import DARK_GRAY, FPS, HEIGHT, LEVEL_MAP, WIDTH

class Game():
    """
    """

    def __init__(self):
        """
        """

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level(LEVEL_MAP)

    def handle_events(self):
        """
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def run(self):
        """
        """

        while True:
            self.handle_events()
            self.screen.fill(DARK_GRAY)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
