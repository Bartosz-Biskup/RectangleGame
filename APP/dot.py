from APP.game_object import GameObject
from APP.physical import NO_MOVEMENT_ITEM
from APP.point import Point
from APP.size import Size


class Dot(GameObject):
    def __init__(self, position: Point, size: int, color: tuple[int, int, int] = (0, 0, 255)):
        left_top: Point = Point(position.x - size // 2, position.y - size // 2)
        super().__init__(left_top, Size(size, size), NO_MOVEMENT_ITEM, "DOT", color)

    def tick(self, *args):
        ...