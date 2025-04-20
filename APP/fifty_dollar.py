from money import Money
from point import Point


class FiftyDollar(Money):
    def __init__(self, position: Point):
        super().__init__(position, 50, "50DOLLAR", "objects/50dollar.png")
