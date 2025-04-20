from dataclasses import dataclass
from math import hypot


@dataclass
class Point:
    x: int
    y: int


def subtract_points(a: Point, b: Point) -> Point:
    return Point(a.x - b.x,
                 a.y - b.y)


def point_distance(a: Point, b: Point) -> float:
    x_axis: int =a.x - b.x
    y_axis: int = a.y - b.y

    return hypot(x_axis, y_axis)



