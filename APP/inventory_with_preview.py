from APP.inventory import Inventory
from APP.item_preview import ItemPreview

# essentials
from point import Point
from APP.item import Item
from APP.static_item import StaticItem

# for types
from APP.stack import Stack


ITEM_SHIFT_PX: int = 70


class InventoryWithPreview(Inventory):
    def __init__(self, size: int, max_stack: int, position: Point):
        super().__init__(size, max_stack)
        self.position: Point = position
        self.size = self.size
        self.pos_x = self.position.x
        self.pos_y = self.position.y
        self.previews: list[ItemPreview] = []

    def tick(self, inventory_pointer: int):
        self.previews: list[ItemPreview] = []
        for i in range(self.size):
            last_index: Item | None = self.last_index(i)
            stack: Stack | None = self[i]
            if stack is not None:
                amount: int = len(stack.stack_content)
            else:
                amount: int = 0
            selected: bool = i == inventory_pointer

            if last_index is not None:
                real_item_preview: ItemPreview = ItemPreview(last_index, Point(self.pos_x + ITEM_SHIFT_PX * i,
                                                                               self.pos_y), selected, amount)
                self.previews.append(real_item_preview)
            else:
                real_item_preview = ItemPreview(None, Point(self.pos_x + ITEM_SHIFT_PX * i,
                                                            self.pos_y), selected, amount)

                self.previews.append(real_item_preview)

    def draw(self, window):
        for i in self.previews:
            i.draw(window)

