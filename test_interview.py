"""Test file for technical interview challenges"""

import pytest

from interview import get_score, assign_tiles, assign_tiles_weighted, BAG


def test_get_correct_score():
    """Checks the function returns the correct score for a given string"""

    assert get_score("GUARDIAN") == 10


def test_incorrect_input():
    """Check error is raised when given an empty string"""

    with pytest.raises(ValueError):
        get_score("")


def test_correct_number_tiles_assigned():
    """Checks whether the correct amount fo tiles are assigned to a player"""

    assert len(assign_tiles()) == 7


def test_correct_type_tiles():
    """Tests to make sure the list contain strings"""

    my_list = assign_tiles()

    assert isinstance(my_list[0], str)


def test_amount_of_tiles_remaining():
    """Tests the amount of remaining tiles after assigning to player"""

    bag_length = len(BAG)
    my_tiles = assign_tiles_weighted()

    assert len(BAG) == bag_length - 7
