from physical import Physical
from point import Point
from size import Size
from walls import Wall


def generate_wall_with_3rd_reich_pattern(point: Point):
    x: int = point.x
    y: int = point.y

    wall = Wall(Point(x, y), Size(50, 15), Physical(0, 0, 0))
    wall1 = Wall(Point(x+50, y), Size(15, 100), Physical(0, 0, 0))
    wall2 = Wall(Point(x+65, y+85), Size(50, 15), Physical(0, 0, 0))
    wall3 = Wall(Point(x, y+50), Size(15, 50), Physical(0, 0, 0))
    wall4 = Wall(Point(x, y+42), Size(115, 15), Physical(0, 0, 0))
    wall5 = Wall(Point(x+100, y), Size(15, 42), Physical(0, 0, 0))

    return [wall, wall1, wall2, wall3, wall4, wall5]
