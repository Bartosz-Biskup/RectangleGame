from APP.game_object import GameObject
from APP.point import Point
from item import Item


class Stack:
    def __init__(self, object: GameObject, max_amount: int) -> None:
        self.item = Item(object, Point(0, 0))
        self.item_id: str = self.item.destination.id
        self.max_amount: int = max_amount
        self.stack_content: list[Item] = [self.item]

    def add(self, object: GameObject) -> bool:
        """
        :param object: object to be added
        :return: True if added
        """
        item = Item(object, Point(0, 0))
        if item.destination.id != self.item_id and len(self.stack_content) != 0:
            return False
        if len(self.stack_content) == self.max_amount:
            return False

        self.stack_content.append(item)
        if len(self.stack_content) == 1:
            self.item = item
            self.item_id = item.destination.id
        return True

    def remove(self) -> Item | None:
        if len(self.stack_content) == 0:
            return None

        return self.stack_content.pop()

    def last_index(self) -> Item | None:
        last: int = len(self.stack_content) - 1

        if last >= 0:
            return self.stack_content[last]
