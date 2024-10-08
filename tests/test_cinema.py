# import sys
# sys.path.insert(0, './')
from pprint import pprint
from copy import deepcopy

import pytest

from cinema import cinema
from helper import print_map, seat_label_from_id, mock_seat_map
from pytest_steps import test_steps

MAP_DEBUG = False


# @pytest.fixture

def debug_map(c1, description, **context):
    """
    print map for debugging
    """
    global MAP_DEBUG
    if MAP_DEBUG != False:
        print("\n=="+description)
        print(print_map(c1, **context))


"""
Test Creating Class
"""


@pytest.mark.parametrize("row, col", [(8, 10), (1, 10), (10, 10), (26, 50)])
def test_cinema_init(row, col):
    c1 = cinema(title="test", row=row, col=col)
    assert c1.row == row
    assert c1.col == col

    assert len(c1.cinema_map) == row
    for r in c1.cinema_map:
        assert len(r) == col

    num_seats = c1.seat_available()
    assert num_seats == (row*col)


"""
Test Creating Class out of boundary
"""


@pytest.mark.parametrize("row, col", [(0, 10), (10, 0), (10, -1), (27, 50), (26, 51)])
def test_cinema_init_invalid(row, col):
    with pytest.raises(ValueError, match="parameters_out_of_bound"):
        c1 = cinema(title="test", row=row, col=col)
    # assert c1 == None


"""
Test auto_booking() function
"""


@pytest.mark.parametrize("title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take",
                         [("Inception", 1, 1, (), "1", 1, 0, 0, ("A1")),
                          ("Inception", 5, 9, (), "1", 4,
                           0, 0, ("A3", "A4", "A5", "A6")),
                          ("Inception", 5, 9, (), "1", 12, 0, 0, ("A1", "A2", "A3",
                           "A4", "A5", "A6", "A7", "A8", "A9", "B4", "B5", "B6")),
                          ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                           "A9", "B4", "B5", "B6"), "1", 4, 0, 0, ("B2", "B3", "B7", "B8")),
                          ("Inception", 5, 8, (), "1", 4,
                           0, 0, ("A3", "A4", "A5", "A6")),
                          ("Inception", 5, 8, (), "1", 12, 0, 0, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B3", "B4", "B5", "B6")), \
                          # cases in the list
                          ("Inception", 8, 10, (), "1", 4, 0, 0, ("A4", "A5", "A6", "A7")), \
                          ("Inception", 8, 10, ("B3", "B4", "B5", "B6"), "2", 12, 0, 0, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B7", "B8")), \
                          ])
def test_auto_booking(title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take):

    c1 = cinema(title=title, row=row, col=col)

    # setup initial seat map
    # pprint ( seats_taken)
    if len(seats_taken) > 0:
        mock_seat_map(c1.cinema_map, row, col, "X", seats=seats_taken)
        # pprint ( c1.cinema_map)
    debug_map(c1, "Initial Map", map_mode=2)

    tmp_map = deepcopy(c1.cinema_map)

    booking_map = c1.auto_booking(num_ticket=num_ticket)
    # pprint ( booking_map)
    debug_map(c1, "Booking Map", map_mode=1, selected=booking_map)

    # booking_id = O for auto book
    mock_seat_map(tmp_map, row, col, "O", seats=seats_to_take)
    debug_map(c1, "Expected Map", map_mode=1, selected=tmp_map)

    # Test if booking is as expected
    assert tmp_map == booking_map


"""
# Invalid auto booking 

e.g. no enough seat due to taken seats. 
"""


@pytest.mark.parametrize("title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take",
                         [("Inception", 1, 1, (), "1", 2, 0, 0, ("A1")),
                          ("Inception", 5, 9, (), "1", 46,
                           0, 0, ("A3", "A4", "A5", "A6")),
                          ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                           "A9", "B4", "B5", "B6"), "1", 35, 0, 0, ("B2", "B3", "B7", "B8"))
                          ])
def test_auto_booking_invalid(title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take):

    c1 = cinema(title=title, row=row, col=col)

    # setup initial seat map
    # pprint ( seats_taken)
    if len(seats_taken) > 0:
        mock_seat_map(c1.cinema_map, row, col, "X", seats=seats_taken)
        # pprint ( c1.cinema_map)
    debug_map(c1, "Initial Map", map_mode=2)

    with pytest.raises(ValueError, match="not_enough_seat"):
        c1.auto_booking(num_ticket=num_ticket)


"""
Test custom_booking() function
Use mock to setup env
=== refactored into end to end flow. ===
"""


"""
Invalid custom_booking 
no enough seat
no enough seat due to starting seats. 
no enough seat due to taken seats. 
"""


@pytest.mark.parametrize("title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take",
                         [
                             ("Inception", 5, 9, (), "1", 4,
                              6, 0, ("A3", "A4", "A5", "A6")),
                             ("Inception", 5, 9, (), "1", 30, 2, 6, ("A1", "A2", "A3",
                              "A4", "A5", "A6", "A7", "A8", "A9", "B4", "B5", "B6")),
                             ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                              "A9", "B4", "B5", "B6"), "1", 34, 1, 0, ("B2", "B3", "B7", "B8")),
                             ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                              "A9", "B4", "B5", "B6"), "1", 40, 0, 0, ("B2", "B3", "B7", "B8"))
                         ])
def test_custom_booking_invalid(title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take):

    c1 = cinema(title=title, row=row, col=col)

    # setup initial seat map
    # pprint ( seats_taken)
    if len(seats_taken) > 0:
        mock_seat_map(c1.cinema_map, row, col, "X", seats=seats_taken)
        # pprint ( c1.cinema_map)
    debug_map(c1, "Initial Map", map_mode=2)

    with pytest.raises(ValueError):
        c1.custom_booking(num_ticket=num_ticket,
                          start_row=start_row, start_col=start_col)


"""
Test save_booking() function
Use mock to setup env
=== Refactored to end to end flow. ===
"""


"""
Test get_booking() function
"""


def test_get_booking_invalid():
    title, row, col = "Inception", 8, 10

    c1 = cinema(title=title, row=row, col=col)
    with pytest.raises(ValueError, match="no_booking"):
        c1.get_booking(5)


"""
Test Booking Flow: add stages of sequential functions incrementally ( alternative to mocking) 
Input: c1 with title, row, col, booked seats 
Steps: Book, review, confirm and get


Cases to consider:
even, odd col 
single, multiple seat
overflow to new line
Mock previous booking 
border condition
"""


@pytest.mark.parametrize("title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take",
                         [("Inception", 1, 1, (), "1", 1, 0, 0, ("A1")),
                          ("Inception", 5, 9, (), "1", 4,
                           0, 0, ("A3", "A4", "A5", "A6")),
                          ("Inception", 5, 9, (), "1", 12, 0, 0, ("A1", "A2", "A3",
                           "A4", "A5", "A6", "A7", "A8", "A9", "B4", "B5", "B6")),
                          ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                           "A9", "B4", "B5", "B6"), "1", 4, 0, 0, ("B2", "B3", "B7", "B8")),
                          ("Inception", 5, 9, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                           "A9", "B4", "B5", "B6"), "1", 4, 1, 4, ("B7", "B8", "B9", "C5")),
                          ("Inception", 5, 8, (), "1", 4,
                           0, 0, ("A3", "A4", "A5", "A6")),
                          ("Inception", 5, 8, (), "1", 12, 0, 0, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B3", "B4", "B5", "B6")), \
                          # cases in the list
                          ("Inception", 8, 10, (), "1", 4, 0, 0, ("A4", "A5", "A6", "A7")), \
                          ("Inception", 8, 10, (), "1", 4, 1, 2, ("B3", "B4", "B5", "B6")), \
                          ("Inception", 8, 10, ("B3", "B4", "B5", "B6"), "2", 12, 0, 0, ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "B7", "B8")), \
                          ("Inception", 8, 10, ("B3", "B4", "B5", "B6"), "2", 12, 1, 4, ("B7",
                           "B8", "B9", "B10", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"))
                          ])
@test_steps('step_booking', 'step_confirm_booking', 'step_get_booking', 'step_count_available')
def test_booking_flow(title, row, col, seats_taken, booking_id, num_ticket, start_row, start_col, seats_to_take):

    c1 = cinema(title=title, row=row, col=col)

    # setup initial seat map
    # pprint ( seats_taken)
    if len(seats_taken) > 0:
        mock_seat_map(c1.cinema_map, row, col, "X", seats=seats_taken)
        # pprint ( c1.cinema_map)
    debug_map(c1, "Initial Map", map_mode=2)

    empty_map = deepcopy(c1.cinema_map)
    org_booking_id = c1.booking_id

    # 1. step_booking
    booking_map = c1.custom_booking(
        num_ticket=num_ticket, start_row=start_row, start_col=start_col)
    # pprint ( booking_map)
    debug_map(c1, "Booking Map", map_mode=1, selected=booking_map)

    # booking_id = O for auto book
    tmp_map = deepcopy(empty_map)
    mock_seat_map(tmp_map, row, col, "O", seats=seats_to_take)
    debug_map(c1, "Expected Map", map_mode=1, selected=tmp_map)

    # Test if booking is as expected
    assert tmp_map == booking_map
    yield

    # 2. step_confirm_booking

    tmp_map = deepcopy(empty_map)
    c1.save_booking(booking_map, booking_id=booking_id)
    mock_seat_map(tmp_map, row, col, booking_id, seats=seats_to_take)
    assert tmp_map == c1.cinema_map
    assert c1.booking_id == org_booking_id+1
    yield

    # 3. step_get_booking
    tmp_map = deepcopy(empty_map)
    mock_seat_map(tmp_map, row, col, "O", seats=seats_to_take)
    mock_seat_map(tmp_map, row, col, "#", seats=seats_taken)
    debug_map(c1, "Get Map", map_mode=1, selected=tmp_map)

    booking_map = c1.get_booking(booking_id)
    # pprint (booking_map)

    assert tmp_map == booking_map
    yield

    # c1.save_booking(  booking_map , booking_id=booking_id)
    # mock_seat_map(tmp_map, row, col, booking_id, seats=seats_to_take)

    # 4. step_count_available
    expected_seats_available = row*col-len(seats_taken)-num_ticket
    assert c1.seat_available() == expected_seats_available
    yield
