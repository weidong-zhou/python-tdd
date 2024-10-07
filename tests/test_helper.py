# import sys
# sys.path.insert(0, './')
from pprint import pprint
from copy import deepcopy

import pytest

from helper import seat_id_from_label, seat_label_from_id,  mock_seat_map


@pytest.mark.parametrize("row, col, label", [(1, 1, "B2"), (2, 10, "C11")])
def test_seat_id_from_label(row, col, label):
    r, c = seat_id_from_label(label)
    assert r == row
    assert c == col


@pytest.mark.parametrize("row, col, label", [(1, 1, "B2"), (2, 10, "C11")])
def test_seat_label_from_id(row, col, label):
    assert seat_label_from_id(row, col) == label


def test_mock_seat_map():
    row, col = 8, 10
    booking_id = "X"
    seats = ("A3", "E4")

    org_map = []
    for r in range(row):
        seat_col = []
        for c in range(col):
            seat_col.append({"booking": None})
        org_map.append(seat_col)

    mock_seat_map(org_map, row, col, booking_id, seats=seats)

    assert org_map[0][2]["booking"] == "X"
    assert org_map[4][3]["booking"] == "X"
