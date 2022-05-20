from Project.models.random_output import user_input, word_list, random_output
from unittest.mock import *
import pytest


@patch("builtins.input", side_effect=["one two three"])
def test_example(mock_input):
    value1 = input()
    assert value1 == "one two three"


def test_list():
    assert word_list("one two three") == ["one", "two", "three"]


def test_random():
    random = random_output(["one", "two", "three"])
    assert random in ["one", "two", "three"]
