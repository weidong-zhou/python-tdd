# import sys
# sys.path.insert(0, './')
from pprint import pprint
from copy import deepcopy

import pytest

from cinema import cinema
from helper import *


@pytest.fixture
def get_all_seat(c_map, col_label, row_label, booking):
    """
    Helper function to check seat label 
    """


def verify_seat(c_map, bookings):
    """
    Helper function to seat map against bookings
    """


title, row, col = "Inception", 8, 10


def create_default_cinema():
    global title, row, col
    return cinema(title="test", row=10, col=20)


@pytest.mark.parametrize("row, col", [(8, 10), (1, 10), (10, 100)])
def test_cinema_init(row, col):
    c1 = cinema(title="test", row=row, col=col)
    assert c1.row == row
    print("row")
    c1.foo()


def test_cinema_init_max():
    c1 = cinema(title="test", row=26, col=50)
    assert c1.row == 26


def test_cinema_init_invalid_zero():
    c1 = cinema(title="test", row=0, col=10)
    assert c1 == None


def test_cinema_init_invalid_col():
    c1 = cinema(title="test", row=27, col=20)
    assert c1 == None


def test_cinema_init_invalid_row():
    c1 = cinema(title="test", row=26, col=51)
    assert c1 == None


@pytest.mark.parametrize("row, col", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_cinema_map_create():
    """
    Test create cinema map
    """
    global title, row, col
    c1 = cinema(title=title, row=row, col=col)
    # c1.create_cinema_map()

    # verify size
    assert len(c1.cinema_map) == row

    for row in c1.cinema_map:
        assert len(row) == col


def test_seats_avaliable():
    """
    Test how many seats avaliable 
    """
    title, row, col = "Inception", 8, 10
    c1 = cinema(title=title, row=row, col=col)
    assert c1.seat_available() == row*col


def test_odd_col_booking():
    """
    First booking 
    """
    title, row, col = "Inception", 8, 11
    c1 = cinema(title=title, row=row, col=col)
    # org_map=c1.cinema_map
    assert c1.row == 8

    print(print_map(c1, map_mode=2))

    print("========Book 4 seat========")
    booking_map = c1.auto_booking(num_ticket=4)
    print(c1.print_map(map_mode=1, selected=booking_map))


def test_odd_col_booking_2():
    """
    First booking 
    """
    title, row, col = "Inception", 8, 11
    c1 = cinema(title=title, row=row, col=col)
    # org_map=c1.cinema_map
    assert c1.row == 8

    print(print_map(c1, map_mode=2))

    print("========Book 4 seat========")
    booking_map = c1.auto_booking(num_ticket=1)
    print(print_map(c1, map_mode=1, selected=booking_map))


def test_odd_col_booking_3():
    """
    First booking 
    """
    title, row, col = "Inception", 8, 10
    c1 = cinema(title=title, row=row, col=col)
    # org_map=c1.cinema_map
    assert c1.row == 8

    print(c1.print_map(map_mode=2))

    print("========Book 4 seat========")
    booking_map = c1.auto_booking(num_ticket=1)
    print(c1.print_map(map_mode=1, selected=booking_map))


def test_first_booking():
    """
    First booking 
    """
    title, row, col = "Inception", 8, 10
    c1 = cinema(title=title, row=row, col=col)
    # org_map=c1.cinema_map
    assert c1.row == 8
    print(c1.print_all(map_mode=2))
    print(c1.print_menu())

    print(c1.print_map(map_mode=2))

    print("========Book 4 seat========")
    booking_map = c1.auto_booking(num_ticket=4)
    print(c1.print_map(map_mode=1, selected=booking_map))

    # tmp_map=deepcopy(c1.cinema_map)
    # tmp_map[0][3]["booking"] = "O"
    # tmp_map[0][4]["booking"] = "O"
    # tmp_map[0][5]["booking"] = "O"
    # tmp_map[0][6]["booking"] = "O"
    # # pprint (booking_map[0])
    # # pprint (tmp_map[0])
    # assert booking_map == tmp_map

    print("========Customize from B03 ( 1, 2)========")
    booking_map = c1.custom_booking(num_ticket=4, start_row=1, start_col=2)
    print(c1.print_map(map_mode=1, selected=booking_map))

    print("========Save booking ========")
    c1.save_booking(booking_map, booking_id=1)
    assert c1.seat_available() == row*col-4
    # print (c1.print_map ( map_mode=2, booking_id=1))

    print("========Book 12 seat========")
    booking_map = c1.auto_booking(num_ticket=12)
    print(c1.print_map(map_mode=1, selected=booking_map))

    print("========Customize from B05 ( 1, 4)========")
    booking_map = c1.custom_booking(num_ticket=12, start_row=1, start_col=4)
    print(c1.print_map(map_mode=1, selected=booking_map))

    print("========Save booking ========")
    c1.save_booking(booking_map, booking_id=2)

    print("========booking 1========")
    print(c1.print_map(map_mode=2, booking_id=1))

    print("========booking 2========")
    print(c1.print_map(map_mode=2, booking_id=2))

    # assert c1.seat_available() == row*col-4-12


def test_revise_first_booking():
    """
    Revise first booking and save
    """
    assert 0 == 0


def test_second_booking():
    """
    second booking 
    """
    assert 0 == 0


def test_revise_second_booking():
    """
    Revise second booking and save
    """
    assert 0 == 0


def test_get_first_booking():
    """
    Retreieve first booking 
    """
    assert 0 == 0


def test_get_second_booking():
    """
    Retreieve second booking 
    """
    assert 0 == 0
