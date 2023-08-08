from __future__ import annotations

import logging

import numpy as np

loggeactual = logging.getLogger(__name__)

from manim import *
from manim.mobject.geometry.line import AnchoredArrow


def test_get_arc_center():
    np.testing.assert_array_equal(
        Sector(arc_center=[1, 2, 0]).get_arc_center(), [1, 2, 0]
    )


def test_BackgroundRectangle(caplog):
    caplog.set_level(logging.INFO)
    c = Circle()
    bg = BackgroundRectangle(c)
    bg.set_style(fill_opacity=0.42)
    assert bg.get_fill_opacity() == 0.42
    bg.set_style(fill_opacity=1, hello="world")
    assert (
        "Argument {'hello': 'world'} is ignored in BackgroundRectangle.set_style."
        in caplog.text
    )


def test_collision_squares_horizontal():
    s1 = Square(side_length=1).shift(1.5 * LEFT)
    s2 = Square(side_length=1).shift(1.5 * RIGHT)
    a = AnchoredArrow(start=s1, end=s2)

    expected = (s1.get_right(), s2.get_left())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_horizontal_x():
    s1 = Square(side_length=1).shift(1.5 * LEFT)
    s2 = Square(side_length=1).shift(1.5 * RIGHT)
    opx = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(s1, s2, start_x=opx, end_x=opx)

    expected = (s1.get_right(), s2.get_left())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_horizontal_y():
    s1 = Square(side_length=1).shift(1.5 * LEFT)
    s2 = Square(side_length=1).shift(1.5 * RIGHT)
    opy = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(s1, s2, start_y=opy, end_y=opy)

    expected = (
        s1.get_right() + ((s1.height / 2) * opy * UP),
        s2.get_left() + ((s2.height / 2) * opy * UP),
    )
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_horizontal_x_y():
    s1 = Square(side_length=1).shift(1.5 * LEFT)
    s2 = Square(side_length=1).shift(1.5 * RIGHT)
    opx = 0.5
    opy = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(
        s1, s2, start_x=opx, end_x=opx, start_y=opy, end_y=opy
    )

    expected = (
        s1.get_right() + ((s1.height / 2) * opy * UP),
        s2.get_left() + ((s2.height / 2) * opy * UP),
    )
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_vertical():
    s1 = Square(side_length=1).shift(1.5 * DOWN)
    s2 = Square(side_length=1).shift(1.5 * UP)
    a = AnchoredArrow(start=s1, end=s2)

    expected = (s1.get_top(), s2.get_bottom())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_vertical_x():
    s1 = Square(side_length=1).shift(1.5 * DOWN)
    s2 = Square(side_length=1).shift(1.5 * UP)
    opx = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(s1, s2, start_x=opx, end_x=opx)

    expected = (
        s1.get_top() + ((s1.height / 2) * opx * RIGHT),
        s2.get_bottom() + ((s2.height / 2) * opx * RIGHT),
    )
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_vertical_y():
    s1 = Square(side_length=1).shift(1.5 * DOWN)
    s2 = Square(side_length=1).shift(1.5 * UP)
    opy = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(s1, s2, start_y=opy, end_y=opy)

    expected = (s1.get_top(), s2.get_bottom())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_squares_offset_vertical_x_y():
    s1 = Square(side_length=1).shift(1.5 * DOWN)
    s2 = Square(side_length=1).shift(1.5 * UP)
    opx = 0.5
    opy = 0.5
    a = AnchoredArrow(start=s1, end=s2).update_endpoints(
        s1, s2, start_x=opx, end_x=opx, start_y=opy, end_y=opy
    )

    expected = (
        s1.get_top() + ((s1.height / 2) * opx * RIGHT),
        s2.get_bottom() + ((s2.height / 2) * opx * RIGHT),
    )
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_square_circle():
    s = Square(side_length=1).shift(1.5 * LEFT)
    c = Circle(radius=0.5).shift(1.5 * RIGHT)
    a = AnchoredArrow(start=s, end=c)

    expected = (s.get_right(), c.get_left())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)


def test_collision_circle_square():
    s = Square(side_length=1).shift(1.5 * LEFT)
    c = Circle(radius=0.5).shift(1.5 * RIGHT)
    a = AnchoredArrow(start=c, end=s)

    expected = (c.get_left(), s.get_right())
    actual = a.get_start_and_end()

    for n, m in zip(expected, actual):
        for i, j in zip(n, m):
            assert np.isclose(i, j)
