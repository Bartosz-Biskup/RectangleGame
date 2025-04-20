from ipaddress import ip_network

from static_text_box import StaticTextBox
from point import Point
from inventory import Inventory
from stack import Stack
from item import Item


def count_net_worth(inventory: Inventory) -> int:
    net_worth: int = 0

    for i in range(inventory.size):
        stack: Stack | None = inventory[i]

        if stack is not None:
            stack_item_type: Item = stack.item
            net_worth += stack_item_type.destination.value * len(stack.stack_content)

    return net_worth


class NetWorthDisplay:
    def __init__(self, position: Point, inventory: Inventory):
        self.inventory = inventory
        self.textbox: StaticTextBox = StaticTextBox(position, (255, 0, 0), 24)

    def tick(self):
        ...

    def draw(self, window, x, y):
        self.textbox.draw(window, f"MONEY: {count_net_worth(self.inventory)}")
