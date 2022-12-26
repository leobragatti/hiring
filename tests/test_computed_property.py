import unittest

from unittest import mock

from src.computed_property import computed_property

mock.patch("src.computed_property.computed_property").start()


class DummyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @computed_property("a", "b", "c")
    def sum(self):
        return sum([self.a, self.b, self.c])


class TestComputedProperty(unittest.TestCase):
    def test_computed_property(self):
        dummy = DummyClass(1, 2, 3)
        self.assertEqual(dummy.sum, 6)
        dummy.y = 10
        self.assertEqual(dummy.sum, 6)
        dummy.a = 10
        self.assertEqual(dummy.sum, 15)
