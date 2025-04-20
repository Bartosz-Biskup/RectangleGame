from item import Item
from stack import Stack
from game_object import GameObject

# essentials
from point import Point


class Inventory:
    def __init__(self, size: int, stack: int):
        self.size = size
        self.max_stack = stack
        self.inventory_content: list[Stack] = []

    def add(self, object: GameObject) -> bool:
        for i in self.inventory_content:
            if i.add(object):
                return True
        else:
            if len(self.inventory_content) != self.size:
                new_stack: Stack = Stack(object, self.max_stack)
                self.inventory_content.append(new_stack)
                return True

        return False

    def remove(self, index: int) -> Item | None:
        if not len(self.inventory_content) > index:
            return None

        return self.inventory_content[index].remove()

    def __getitem__(self, index: int) -> Stack | None:
        if not len(self.inventory_content) > index:
            return None

        stack_content: Stack = self.inventory_content[index]
        last_index: int = len(stack_content.stack_content) - 1

        if last_index >= 0:
            return stack_content

    def last_index(self, i: int):
        try:
            return self.inventory_content[i].stack_content[::-1][0]
        except:
            return None