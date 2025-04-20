from game_object import *
from physical import NO_MOVEMENT_ITEM
from point import Point
from size import Size
from typing import TypeVar


ITEM_WIDTH: int = 50
ITEM_HEIGHT: int = 50
GAME_OBJECT_OR_CHILD = TypeVar("GAME_OBJECT_OR_CHILD", bound=GameObject)


class Item(GameObject):
    def __init__(self, destination: GAME_OBJECT_OR_CHILD, position: Point):
        self.destination: GameObject = destination
        image_path = f"./items/{self.destination.id}.png"
        super().__init__(position, Size(ITEM_WIDTH, ITEM_HEIGHT), NO_MOVEMENT_ITEM, "ITEM", (0, 0, 0), image_path)
        self.loaded = pygame.transform.rotate(pygame.image.load(image_path), 45)

    def unpack_item(self, position: Point) -> GAME_OBJECT_OR_CHILD:
        self.destination.position = position
        return self.destination

    def tick(self):
        ...

    def draw(self, window: pygame.Surface, offset_x, offset_y):
        super().draw(window, offset_x, offset_y)




