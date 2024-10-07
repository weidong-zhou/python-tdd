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
End to end flow
"""


@pytest.mark.parametrize("inputs", [
    ("INCEPTION 8 10\n3\n"),
    ("INCEPTION 8 10\n1\n4\nB03\n\n3\n"),
    ("INCEPTION 8 10\n1\n4\nB03\n\n1\n77\n12\nB05\n\n3\n"),
    ("INCEPTION 8 10\n1\n4\nB03\n\n1\n77\n12\nB05\n\n2\nGIC0001\nGIC0002\n\n3\n"),
])
def test_booking_suite(monkeypatch, inputs):

    b1 = booking_flow()

    inputs_string = StringIO(inputs)
    monkeypatch.setattr('sys.stdin', inputs_string)
    b1.main()
