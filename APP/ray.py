from typing import Optional
import pygame
import math

from APP.DEBUG import DEBUG
from APP.dot import Dot
from APP.game_object import GameObject
from APP.point import Point


def line_start_end_position(center: Point, length: int, angle_deg: int) -> tuple[Point, Point]:
    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad) * length / 2
    dy = math.sin(angle_rad) * length / 2

    x1 = center.x - dx
    y1 = center.y - dy
    x2 = center.x + dx
    y2 = center.y + dy

    return Point(int(x1), int(y1)), Point(int(x2), int(y2))


class Ray:
    def __init__(self, length: int, angle: int, center_position: Point):
        self.length = length
        self.angle = angle % 360
        self.position = center_position  # this is the center of the line
        self.dot = Dot(self.position, 10)

        # Get start and end points of the rotated line
        self.start, self.end = line_start_end_position(self.position, self.length, self.angle)

        # Create base horizontal surface
        self.base_ray = pygame.Surface((self.length, 1), pygame.SRCALPHA)
        self.base_ray.fill((255, 255, 255))  # white pixel line for mask

        # Rotate the surface
        self.rotated_ray = pygame.transform.rotate(self.base_ray, -self.angle)

        # Calculate new rect after rotation (to know where the top-left is)
        self.rotated_rect = self.rotated_ray.get_rect(center=(self.position.x, self.position.y))

        # Create the mask
        self.ray_mask = pygame.mask.from_surface(self.rotated_ray)

    def overlap(self, other: GameObject) -> Optional[Point]:
        other_surface = pygame.Surface((other.size.width, other.size.height), pygame.SRCALPHA)
        other_surface.fill((255, 255, 255))  # full mask

        other_mask = pygame.mask.from_surface(other_surface)

        # Offset is relative to top-left of rotated surface
        x_offset = other.position.x - self.rotated_rect.left
        y_offset = other.position.y - self.rotated_rect.top

        overlap_point: Optional[Point] = self.ray_mask.overlap(other_mask, (x_offset, y_offset))
        if overlap_point is not None:
            return Point(self.position.x + x_offset,
                         self.position.y + y_offset)

    def draw(self, window: pygame.Surface, x_shift: int, y_shift: int):
        pygame.draw.line(window,
                         (255, 0, 0),
                         (self.start.x - x_shift, self.start.y - y_shift),
                         (self.end.x - x_shift, self.end.y - y_shift))

        if DEBUG:
            self.dot.draw(window, x_shift, y_shift)

