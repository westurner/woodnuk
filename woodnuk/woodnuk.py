"""Main module."""

import math
import numbers
from fractions import Fraction


def nominalstr2fraction(nominalstr):
    _str = nominalstr.rstrip('"')
    isnegative = False
    if _str[0] == "-":
        isnegative = True
        _str = _str[1:]
    components = _str.split("-", 1)
    value = Fraction(components.pop(0))
    if components:
        value += Fraction(components.pop())
    if isnegative:
        value *= -1
    return value


def express_in(number: numbers.Number, tostr=True, cls=None):
    if cls is None:
        cls = number.__class__
    _floor = math.floor(number)
    _remaining = cls(number - _floor)
    if _floor == 0:
        _remaining = cls(_remaining)
        if tostr:
            return '%s"' % _remaining
        else:
            return cls(_remaining)
    if tostr:
        if _remaining:
            return '%s-%s"' % (_floor, _remaining)
        else:
            return '%s"' % (_floor)
    else:
        return (_floor, _remaining)


class Number(Fraction):
    def __new__(cls, *args):
        numerator = args[0]
        if len(args) == 1 or args[1] is None:
            if isinstance(numerator, str):
                if "-" in numerator:
                    _args = list(args)
                    _args[0] = nominalstr2fraction(numerator)
                    args = _args
                    # return Number(nominal2fraction(numerator))
        return super().__new__(cls, *args)

    # def __str__(self):
    #    return express_in(self, tostr=True)


