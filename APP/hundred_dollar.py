from money import Money
from point import Point


class HundredDollar(Money):
    def __init__(self, position: Point):
        super().__init__(position, 100, "100DOLLAR", "objects/100dollar.png")
