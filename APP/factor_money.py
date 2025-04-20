from APP.fifty_dollar import FiftyDollar
from hundred_dollar import HundredDollar

from point import Point
from random import randint


def factor_money(point: Point):
    if randint(0, 1) == 0:
        return HundredDollar(point)
    else:
        return FiftyDollar(point)
