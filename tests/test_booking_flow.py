# import sys
# sys.path.insert(0, './')
from pprint import pprint
from copy import deepcopy

import pytest
import sys
from io import StringIO
from booking_flow import booking_flow
from helper import print_map, seat_label_from_id, mock_seat_map
from pytest_steps import test_steps


"""
Test input params
Working case
"""


@pytest.mark.parametrize("inputs,title, row, col", [
    ("INCEPTION 8 10", "INCEPTION", 8, 10),
    ("INCEPTION XXX 8 10", "INCEPTION XXX", 8, 10)
])
def test_get_cinema_paras(monkeypatch, inputs, title, row, col):
    inputs_string = StringIO("{} {} {}\n".format(title, row, col))
    monkeypatch.setattr('sys.stdin', inputs_string)

    b1 = booking_flow()
    b1.get_cinema_params()
    print(b1.title)
    assert b1.title == title
    assert b1.row == row
    assert b1.col == col


"""
Test input params
This would ask for input again
"""


@pytest.mark.parametrize("inputs", [("INCEPTION8 10"), ("INCEPTION [8] [10]"),])
def test_get_cinema_paras(monkeypatch, inputs):
    inputs_string = StringIO("{}\n".format(inputs))
    monkeypatch.setattr('sys.stdin', inputs_string)

    b1 = booking_flow()
    with pytest.raises(EOFError):
        b1.get_cinema_params()


"""
Test booking flow
Increamental working case
1: New booking
2. change booking
3. +1 new booking 
4. change booking, accept
All -> check booking 1
"""


@pytest.mark.parametrize("cinema_inputs, inputs, inputs_2, inputs_3, inputs_4, seats_to_take, seats_to_take_2", [
    ("INCEPTION 8 10\n", "4\n\n", "", "", "", ("A4", "A5", "A6", "A7"), ()),
    ("INCEPTION 8 10\n", "4\nB03\n\n", "", "", "", ("B3", "B4", "B5", "B6"), ()),
    ("INCEPTION 8 10\n", "4\nB03\n\n", "12\n\n", "", "", ("B3", "B4", "B5", "B6"),
     ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B7", "B8")),
    ("INCEPTION 8 10\n", "4\nB03\n\n", "12\nB05\n\n", "GIC0001\nGIC0002\n\n", "", ("B3", "B4", "B5", "B6"),
     ("B7", "B8", "B9", "B10", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9")),
])
# ("INCEPTION 8 10\n", "4\n\n", ("A4", "A5", "A6", "A7")),
# ("INCEPTION 8 10\n", "4\nB03\n\n", ("B3", "B4", "B5", "B6"))
def test_new_booking(monkeypatch, cinema_inputs, inputs, inputs_2, inputs_3, inputs_4, seats_to_take, seats_to_take_2):

    b1 = booking_flow()

    inputs_string = StringIO(cinema_inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.get_cinema_params()

    c1 = b1.cinema

    expected_map = deepcopy(c1.cinema_map)
    mock_seat_map(expected_map, c1.row, c1.col, 1, seats=seats_to_take)

    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.new_booking()

    # pprint(c1.cinema_map)

    assert expected_map == c1.cinema_map

    if inputs_2 != "":
        inputs_string = StringIO(inputs_2)
        monkeypatch.setattr('sys.stdin', inputs_string)
        b1.new_booking()
        mock_seat_map(expected_map, c1.row, c1.col, 2, seats=seats_to_take_2)
        assert expected_map == c1.cinema_map

    if inputs_3 != "":
        inputs_string = StringIO(inputs_3)
        monkeypatch.setattr('sys.stdin', inputs_string)
        b1.get_booking()

    # pprint(c1.cinema_map)

    # @test_steps('step_booking', 'step_change_booking', 'step_get_booking', 'step_count_available')


"""
1. Book more than available 
2. starting seat out of index 
"""


@pytest.mark.parametrize("cinema_inputs, inputs, inputs_2, inputs_3, inputs_4, seats_to_take, seats_to_take_2, msg", [
    ("INCEPTION 8 10\n", "4\nB03\n\n", "77\n12\n\n", "", "", ("B3", "B4", "B5", "B6"),
     ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B7", "B8"), "Sorry, there are only 76 seats available"),
    ("INCEPTION 8 10\n", "4\nB03\n\n", "12\nZ10\n", "", "", ("B3", "B4", "B5", "B6"),
     ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B7", "B8"), "Sorry, there are only 76 seats available"),

])
# ("INCEPTION 8 10\n", "4\n\n", ("A4", "A5", "A6", "A7")),
# ("INCEPTION 8 10\n", "4\nB03\n\n", ("B3", "B4", "B5", "B6"))
def test__new_booking(capsys, monkeypatch, cinema_inputs, inputs, inputs_2, inputs_3, inputs_4, seats_to_take, seats_to_take_2, msg):

    b1 = booking_flow()

    inputs_string = StringIO(cinema_inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.get_cinema_params()

    c1 = b1.cinema

    expected_map = deepcopy(c1.cinema_map)
    mock_seat_map(expected_map, c1.row, c1.col, 1, seats=seats_to_take)

    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.new_booking()

    if inputs_2 != "":
        inputs_string = StringIO(inputs_2)
        monkeypatch.setattr('sys.stdin', inputs_string)
        capsys.readouterr()
        b1.new_booking()
        out, err = capsys.readouterr()
        assert msg in out


"""
press return to exit new_booking
"""


def test_booking_return(monkeypatch):

    b1 = booking_flow()

    cinema_inputs = "INCEPTION 8 10\n"
    inputs_string = StringIO(cinema_inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.get_cinema_params()

    inputs = "\n"
    c1 = b1.cinema
    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.new_booking()


def testx_get_booking(capsys, monkeypatch):

    b1 = booking_flow()

    cinema_inputs = "INCEPTION 8 10\n"
    inputs_string = StringIO(cinema_inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.get_cinema_params()

    inputs = "GIC0099\n\n"
    # c1 = b1.cinema
    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.get_booking()

    out, err = capsys.readouterr()
    assert "Error find booking ID!" in out


"""
End to end flow
"""


@pytest.mark.parametrize("inputs", [
    ("INCEPTION 8 10\n1\n4\nB03\n\n1\n77\n12\nB05\n\n2\nGIC0001\nGIC0002\n\n3\n"),
])
def test_booking_suite(monkeypatch, inputs):

    b1 = booking_flow()

    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.main()
