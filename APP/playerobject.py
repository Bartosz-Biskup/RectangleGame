# for using
from game_object import GameObject
from net_worth_counter import NetWorthDisplay
from adjust_to_fps import adjustFPS
from inventory_with_preview import InventoryWithPreview

# essentials
from physical import Physical
from size import Size
from point import Point

# libraries
import pygame
from random import randint

# for type hinting
from item import Item


def item_dropped_position():
    return randint(50, 100)


class PlayerObject(GameObject):
    def __init__(self, position: Point,
                 size: Size,
                 movement: Physical,
                 color: tuple[int, int, int],
                 image = None):
        super().__init__(position, size, movement, "PLAYER", color, image)
        self.move = False
        self.image = image

    def tick(self, window, fps):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            self.move = True
            self.movement.velocity += adjustFPS(self.movement.acceleration, 60, fps)
            self.movement.velocity = min(self.movement.max_velocity, self.movement.velocity)
        else:
            self.move = False
            self.movement.velocity = 0

        real_velocity: int = round(adjustFPS(self.movement.velocity, 60, fps))

        if keys[pygame.K_w]:
            self.position.y -= real_velocity
        if keys[pygame.K_s]:
            self.position.y += real_velocity
        if keys[pygame.K_a]:
            self.position.x -= real_velocity
        if keys[pygame.K_d]:
            self.position.x += real_velocity

        self.rect = self.rect = pygame.rect.Rect((self.position.x, self.position.y),
                                     (self.size.width, self.size.height))

    def draw(self, window, x_shift: int, y_shift: int):
        super().draw(window, x_shift, y_shift)


class Player(PlayerObject):
    def __init__(self,
                 position: Point,
                 size: Size,
                 movement: Physical,
                 color: tuple[int, int, int],
                 image = "./objects/player.png"):
        super().__init__(position, size, movement, color, image)
        self.inventory_pointer: int = 0
        self.inventory: InventoryWithPreview = InventoryWithPreview(5, 4, Point(10, 10))
        self.net_worth_label: NetWorthDisplay = NetWorthDisplay(Point(10, 75), self.inventory)

    def collect(self, object: GameObject) -> bool:
        """
        :param object: object to be collected
        :return: True if collected properly
        """
        is_item_added: bool = self.inventory.add(object)

        return is_item_added

    def drop(self):
        """
        :return: removed item of type Item or None
        """
        removed_item: Item | None = self.inventory.remove(self.inventory_pointer)

        return removed_item

    def tick(self, window: pygame.Surface, fps: float, keys: tuple) -> list[Item]:
        """
        :param window: game window
        :param fps: game fps
        :return: list of game objects summoned by player
        """
        super().tick(window, fps)

        if pygame.K_1 in keys:
            self.inventory_pointer = 0
        elif pygame.K_2 in keys:
            self.inventory_pointer = 1
        elif pygame.K_3 in keys:
            self.inventory_pointer = 2
        elif pygame.K_4 in keys:
            self.inventory_pointer = 3
        elif pygame.K_5 in keys:
            self.inventory_pointer = 4
        elif pygame.K_6 in keys:
            self.inventory_pointer = 5
        elif pygame.K_7 in keys:
            self.inventory_pointer = 6
        elif pygame.K_8 in keys:
            self.inventory_pointer = 7
        elif pygame.K_9 in keys:
            self.inventory_pointer = 8
        elif pygame.K_LEFT in keys:
            self.inventory_pointer -= 1
        elif pygame.K_RIGHT in keys:
            self.inventory_pointer += 1

        self.inventory_pointer = self.inventory_pointer % self.inventory.size
        self.inventory.tick(self.inventory_pointer)

        self.net_worth_label.tick()
        self.net_worth_label.draw(window, 0, 0)

        if pygame.K_q in keys and len(self.inventory.inventory_content) > 0:
            removed_item: Item | None = self.drop()

            if removed_item is not None:
                return [removed_item]

        return []

    def draw(self, window, x_shift: int, y_shift: int):
        super().draw(window, x_shift, y_shift)

        item_hold: Item = self.inventory.last_index(self.inventory_pointer)

        if item_hold is not None:
            item_hold.set_position(self.position.x + 15, self.position.y + 15)
            item_hold.draw(window, x_shift, y_shift)

        self.inventory.draw(window)













