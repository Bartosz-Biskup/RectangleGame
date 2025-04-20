from game_object import *

from physical import Physical
from point import Point
from size import Size

MONEY_WIDTH: int = 100
MONEY_HEIGHT: int = 50


class Money(GameObject):
    def __init__(self,
                 position: Point,
                 value: int,
                 id: str,
                 image: str):
        super().__init__(position,
                         Size(MONEY_WIDTH, MONEY_HEIGHT),
                         Physical(0, 0, 0),
                         id,
                         (0, 255, 0),
                         image)
        self.value = value


    def tick(self, object: GameObject):
        self.rect = pygame.rect.Rect((self.position.x, self.position.y), (self.size.width, self.size.height))
        if object.rect.colliderect(self.rect):
            return True

    def draw(self, window, x_offset, y_offset):
        super().draw(window, x_offset, y_offset)




