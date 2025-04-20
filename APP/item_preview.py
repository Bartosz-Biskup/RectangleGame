from item import Item
from static_item import StaticItem

from physical import NO_MOVEMENT_ITEM
from point import Point
from size import Size
from static_object import StaticObject
from static_text_box import StaticTextBox


NON_SELECTED_COLOR: tuple[int, int, int] = (127, 127, 127)
SELECTED_COLOR: tuple[int, int, int] = (80, 80, 80)
FRAME_IMAGE_NOT_SELECTED: str = "./objects/frame.png"
FRAME_IMAGE_SELECTED: str = "./objects/frame_selected.png"
ITEM_AMOUNT_INFO_COLOR: tuple[int, int, int] = (255, 0, 0)
ITEM_FRAME_PX: int = 60


class ItemPreview:
    def __init__(self, item: Item | None, position: Point, selected: bool, item_amount: int):
        self.item = item
        self.position = position
        self.selected = selected
        self.color = SELECTED_COLOR if selected else NON_SELECTED_COLOR
        self.image_path = FRAME_IMAGE_SELECTED if selected else FRAME_IMAGE_NOT_SELECTED
        if item is not None:
            self.static_item: StaticItem = StaticItem(self.item.destination, Point(position.x-5, position.y-5))
        self.frame: StaticObject = StaticObject(self.position,
                                                Size(ITEM_FRAME_PX, ITEM_FRAME_PX),
                                                NO_MOVEMENT_ITEM,
                                                "ITEM_PREVIEW_FRAME",
                                                self.color,
                                                self.image_path)
        self.item_amount: int = item_amount
        self.amount_text_box = StaticTextBox(Point(self.position.x+40, self.position.y+30),
                                             ITEM_AMOUNT_INFO_COLOR,
                                             24)

    def tick(self):
        ...

    def draw(self, window):
        self.frame.draw(window, 0, 0)
        if self.item is not None:
            self.static_item.draw(window, 0, 0)
        if self.item_amount > 0:
            self.amount_text_box.draw(window, str(self.item_amount))
