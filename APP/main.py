import typing
from collections.abc import Iterable
from random import randint

from playerRayCollider import PlayerRayCollider
from factor_money import factor_money
from game_object import GameObject
import pygame
from sound import play_sound
from playerobject import Player
from wall_with_3rd_reich_pattern import generate_wall_with_3rd_reich_pattern
from windowProcess import WindowProcessHandler
from money import Money
from scrollingBackground import ScrollingBackground
from walls import Wall
from PressHandler import KeyPressHandler
from ray import Ray

from point import Point
from physical import *
from size import Size


GAME_OBJECT_OR_CHILD = typing.TypeVar("GAME_OBJECT_OR_CHILD", bound=GameObject)


def get_fps(clock):
    fps = round(1000 // (clock.get_time() + 0.01))
    while fps == 0:
        fps = round(1000 // (clock.get_time() + 0.01))

    return fps


def init_player(x, y, width, height, color):
    return Player(Point(x, y),
                        Size(width, height),
                        Physical(8, 8, 8),
                        color)


def generate_objects_in_repeatable_pattern(generation_function: typing.Callable[[Point], GAME_OBJECT_OR_CHILD | list[GAME_OBJECT_OR_CHILD]],
                                           distance_x: int,
                                           distance_y: int,
                                           start: Point = Point(0, 0),
                                           end: Point = Point(5000, 5000)) -> list[GAME_OBJECT_OR_CHILD]:
    objects: list[GameObject] = []
    start_x: int = start.x
    start_y: int = start.y
    end_x: int = end.x
    end_y: int = end.y

    for i in range(start_x, end_x, distance_x):
        for j in range(start_y, end_y, distance_y):
            object: list[GAME_OBJECT_OR_CHILD] | GameObject = generation_function(Point(i, j))
            if isinstance(object, Iterable):
                objects.extend(object)
            else:
                objects.append(object)

    return objects


def generate_borders(map_end: Point = Point(5000, 5000)) -> list[Wall]:
    walls_to_be_returned: list[Wall] = [Wall(Point(-1, 0), Size(1, map_end.y), NO_MOVEMENT_ITEM),
                                        Wall(Point(0, -1), Size(map_end.x, 1), NO_MOVEMENT_ITEM),
                                        Wall(Point(map_end.x + 1, 0), Size(10, map_end.y), NO_MOVEMENT_ITEM),
                                        Wall(Point(0, map_end.y + 1), Size(map_end.x, 10), NO_MOVEMENT_ITEM)]

    return walls_to_be_returned


window = pygame.display.set_mode((800, 600))
steve: Player = init_player(50, 50, 50, 50, (0, 0, 0))
walls: list[Wall] = generate_objects_in_repeatable_pattern(generate_wall_with_3rd_reich_pattern, 200, 200)
cash: list[Money] = generate_objects_in_repeatable_pattern(factor_money, 300, 300)
walls.extend(generate_borders())

clock = pygame.time.Clock()
windowHandler = WindowProcessHandler()
scrolling_background = ScrollingBackground(steve, Size(800, 600))
keypress_handler: KeyPressHandler = KeyPressHandler()

ray = Ray(400, 45, Point(395, 400))

if __name__ == '__main__':
    run: bool = True
    while run:
        fps: int = get_fps(clock)
        tick_time: int = clock.get_time()
        clock.tick(244)
        window.fill((255, 255, 255))
        screen_position = scrolling_background.tick(walls, Size(800, 600))
        events: list[pygame.event.Event] = pygame.event.get()
        keys = keypress_handler.tick(events)

        if windowHandler.tick(events):
            run = False

        for i in walls:
            i.tick(steve)
            i.draw(window, screen_position.x, screen_position.y)

        for i in cash:
            if i.tick(steve):
                if steve.collect(i):
                    cash.remove(i)
                    play_sound("./sounds/money_dropping.mp3")
            i.draw(window, screen_position.x, screen_position.y)

        for i in steve.tick(window, fps, keys):
            steve_position: Point = steve.get_position()
            steve_x, steve_y = steve_position.x, steve_position.y

            steve_x -= randint(50, 100)
            steve_y -= randint(50, 100)

            drop_destination: Point = Point(steve_x, steve_y)

            if i.destination.id == "100DOLLAR" or i.destination.id == "50DOLLAR":
                cash.append(i.unpack_item(drop_destination))

        steve.draw(window, screen_position.x, screen_position.y)
        ray.draw(window, screen_position.x, screen_position.y)
        print(PlayerRayCollider.does_ray_collide(ray, steve, walls))

        pygame.display.update()
