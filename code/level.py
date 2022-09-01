import pygame
from settings import TILE_SIZE
from tile import Tile

class Level():
    """
    """

    def __init__(self, level_data):
        """
        """

        self.display_surface = pygame.display.get_surface()
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        """
        """

        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):

            for column_index, column in enumerate(row):
                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if column == "X":
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)

    def run(self):
        """
        """

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
