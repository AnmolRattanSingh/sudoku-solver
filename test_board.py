"""
Tests for the data analysis functions
"""
import pytest
from board import Board

GET_NUM_CASES = [
    # test that order of number is from left to right
    ("1j2k3l4k5", 12345),

    # test that correct number is returned when whitespaces are present
    ("kj k23 122", 23122),

    # test that an already clean string comes out the same
    ("12345", 12345),
]

@pytest.mark.parametrize("get_num_test, get_num_result", GET_NUM_CASES)
def test_get_num(get_num_test, get_num_result):
    """
    Test the get_num function which filters out numbers in a string.
    """
    assert get_num(get_num_test) == get_num_result


@pytest.mark.parametrize("genres_test, genres_result", GENRES_CASES)
def test_genres_over_career(genres_test, genres_result):
    """
    Test output of genres_over_career function which returns a
    dictionary containing an actor's movie genre information.
    """
    assert genres_test == genres_result


@pytest.mark.parametrize("box_office_test, box_office_result", BOX_CASES)
def test_box_office_over_time(box_office_test, box_office_result):
    """
    Test output of box_office_over_time function which returns a
    dictionary containing box office collection of actor per year.
    """
    assert box_office_test == box_office_result

    # test years in the dictionary keys are sorted correctly
    assert int(list(box_office_test_dict.keys())[0].split("–")[
               0]) <= int(list(box_office_test_dict.keys())[-1].split("–")[0])


@pytest.mark.parametrize("ratings_test, ratings_result", RATINGS_CASES)
def test_movie_ratings_over_time(ratings_test, ratings_result):
    """
    Test output of movie_ratings_over_time function which returns a
    dictionary containing all the movie ratings over an actor's career.
    """
    assert ratings_test == ratings_result
