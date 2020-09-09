#!/usr/bin/env python

"""Tests for `woodnuk` package."""

import math
from fractions import Fraction

import pytest


from woodnuk import woodnuk
from woodnuk import nominalstr2fraction, express_in, Number

try:
    from sympy import Rational
except ImportError:
    Rational = Fraction


@pytest.mark.parametrize("inputval, expected_output", [
    ['3/2', Fraction("3/2")],
    ['1-1/2"', Fraction("3/2")],
    ['1-1/2', Fraction("3/2")],
    ['-1/2', Fraction("-1/2")],
    ['-1-1/2', Fraction("-3/2")],
    ['0.32', Fraction("8/25")],
    ['0.32', Fraction("32/100")],
    ['0.33', Fraction("33/100")],
    # [1/3, Fraction("1/3")], # AttributeError
])
def test_nominalstr2fraction(inputval, expected_output):
    output = nominalstr2fraction(inputval)
    assert output == expected_output


@pytest.mark.parametrize("number, tostr, expected_output", [
    [Rational("7/2"), False, (3, Rational("1/2"))],
    [0.5625, False, Rational("9/16")],
])
def test_express_in(number, tostr, expected_output):
    output = express_in(number, tostr)
    assert output == expected_output


@pytest.mark.parametrize("inputval, expected_output", [
    ['1-1/2"', Fraction("3/2")],
    ['1-1/2"', Number("3/2")]
])
def test_number(inputval, expected_output):
    output = Number(inputval)
    assert output == expected_output

