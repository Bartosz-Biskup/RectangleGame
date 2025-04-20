import pygame

from game_object import GameObject
from item import ITEM_WIDTH, ITEM_HEIGHT
from physical import NO_MOVEMENT_ITEM
from point import Point
from size import Size
from static_object import StaticObject


class StaticItem(StaticObject):
    def __init__(self, destination: GameObject, position: Point):
        self.destination: GameObject = destination
        image_path = f"./items/{self.destination.id}.png"
        super().__init__(position, Size(ITEM_WIDTH, ITEM_HEIGHT), NO_MOVEMENT_ITEM, "ITEM", (0, 0, 0), image_path)
        self.loaded = pygame.transform.rotate(pygame.image.load(image_path), 45)

    def unpack_item(self, position: Point) -> GameObject:
        self.destination.position = position
        return self.destination

    def tick(self):
        ...

    def draw(self, window: pygame.Surface, offset_x, offset_y):
        super().draw(window, offset_x, offset_y)
