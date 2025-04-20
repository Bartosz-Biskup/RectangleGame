from game_object import *
import pygame
from random import randint
from playerobject import PlayerObject


def generate_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Wall(GameObject):
    def __init__(self, position, size, movement):
        super().__init__(position, size, movement, "WALL", generate_random_color())
        self.rect = pygame.rect.Rect((position.x, position.y), (size.width, size.height))

    def tick(self, *args):
        player: PlayerObject = args[0]

        if player.rect.colliderect(self.rect):
            player_x, player_y = player.get_position().x, player.get_position().y
            player_width, player_height = player.size.width, player.size.height
            wall_x, wall_y = self.get_position().x, self.get_position().y
            wall_width, wall_height = self.size.width, self.size.height

            # Calculate overlaps for each side
            overlap_left = (player_x + player_width) - wall_x
            overlap_right = (wall_x + wall_width) - player_x
            overlap_top = (player_y + player_height) - wall_y
            overlap_bottom = (wall_y + wall_height) - player_y

            # Determine the smallest overlaps for horizontal and vertical axes
            dx = min(overlap_left, overlap_right)
            dy = min(overlap_top, overlap_bottom)

            # Resolve collision along the axis with the smallest overlap
            if dx <= dy:
                if overlap_left < overlap_right:
                    new_x = wall_x - player_width  # Align player's right to wall's left
                else:
                    new_x = wall_x + wall_width  # Align player's left to wall's right
                player.set_position(new_x, player_y)
            else:
                if overlap_top < overlap_bottom:
                    new_y = wall_y - player_height  # Align player's bottom to wall's top
                else:
                    new_y = wall_y + wall_height  # Align player's top to wall's bottom
                player.set_position(player_x, new_y)

    def draw(self, window, x_shift, y_shift):
        super().draw(window, x_shift, y_shift)
