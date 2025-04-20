import pygame

from game_object import GameObject
from physical import Physical
from point import Point
from size import Size


class StaticObject(GameObject):
    def __init__(self,
                 position: Point,
                 size: Size,
                 movement: Physical,
                 id: str,
                 color: tuple[int, int, int],
                 image_path: str = None,
                 ):
        super().__init__(position, size, movement, id, color, image_path)

    def tick(self, *args):
        super().tick(args)

    def draw(self, window, x_shift: int, y_shift: int):
        if self.image is None:
            rect = pygame.rect.Rect((self.position.x, self.position.y),
                                    (self.size.width, self.size.height))

            pygame.draw.rect(window, self.color, rect)
        else:
            window.blit(self.loaded, (self.position.x, self.position.y))
