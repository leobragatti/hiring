import unittest

import os

from collections.abc import Iterable
from unittest import mock

from src.last_lines import last_lines


class TestLastLines(unittest.TestCase):
    def setUp(self) -> None:
        self.random_data = os.getrandom(10000)
        return super().setUp()

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            for line in last_lines("my_files.txt"):
                self.assertIsNotNone(line)

    def test_read_data(self):
        random_data = os.getrandom(10000).decode(errors="ignore")
        mocked_data = mock.mock_open(read_data=random_data)
        mocked_data.return_value.tell.return_value = len(random_data)
        with mock.patch("builtins.open", mocked_data) as mocked:
            with open("input.txt") as tmp:
                lines = last_lines(tmp)
                self.assertIsInstance(lines, Iterable)
                mocked.assert_called_once_with("input.txt")
                random_lines = [f"{item}\n" for item in random_data.split("\n")[::-1]]
                read_data = [line for line in lines]
                self.assertEqual(len(read_data), len(random_lines))
