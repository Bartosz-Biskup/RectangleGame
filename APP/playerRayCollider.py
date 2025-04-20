from typing import Optional

from APP.game_object import GameObject
from APP.walls import Wall
from ray import Ray
from point import *


class PlayerRayCollider:
    def __init__(self, rays: list[Ray]):
        self.rays = rays

    @staticmethod
    def does_ray_collide(ray: Ray, focus: GameObject, obstacles: list[Wall]) -> bool:
        # instantly returns False if focus object doesn't overlap ray
        if ray.overlap(focus) is None:
            return False
        else:
            focus_overlap_point: Point = ray.overlap(focus)

        # get list of obstacles point overlapping to check distance
        list_of_overlapping_points: list[Point] = []
        for i in obstacles:
            overlap_point: Optional[Point] = ray.overlap(i)
            if overlap_point is not None:
                list_of_overlapping_points.append(overlap_point)

        # iterate through all obstacles overlapping and check if its distance is shorter or are in the same quarter as focus
        focus_to_ray_distance: float = point_distance(focus_overlap_point, ray.position)
        for i in list_of_overlapping_points:
            x_quarter_focus: bool = focus.position.x > ray.position.x
            y_quarter_focus: bool = focus.position.y > ray.position.y
            x_quarter_obstacle: bool = i.x > ray.position.x
            y_quarter_obstacle: bool = i.y > ray.position.y


            if point_distance(i, ray.position) < focus_to_ray_distance and x_quarter_focus == x_quarter_obstacle and y_quarter_focus == y_quarter_obstacle:
                return False

        return True
