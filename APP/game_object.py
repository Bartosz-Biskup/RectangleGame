from abc import ABC, abstractmethod
import pygame

from physical import Physical
from point import Point
from size import Size


pygame.init()
pygame.font.init()


class GameObject(ABC):
    def __init__(self,
                 position: Point,
                 size: Size,
                 movement: Physical,
                 id: str,
                 color: tuple[int, int, int],
                 image_path: str = None,
                 ):
        self.position = position
        self.size = size
        self.movement = movement
        self.id = id
        self.image = image_path
        self.color = color

        self.rect = pygame.rect.Rect((self.position.x, self.position.y),
                                     (self.size.width, self.size.height))

        if self.image is not None:
            self.loaded = pygame.image.load(self.image)

    @abstractmethod
    def tick(self, *args):
        ...

    def draw(self, window, x_shift: int, y_shift: int):
        if self.image is None:
            rect = pygame.rect.Rect((self.position.x - x_shift, self.position.y - y_shift),
                                    (self.size.width, self.size.height))

            pygame.draw.rect(window, self.color, rect)
        else:
            window.blit(self.loaded, (self.position.x - x_shift, self.position.y - y_shift))

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = Point(x, y)
