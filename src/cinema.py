from pprint import pprint
from copy import deepcopy

from helper import render_template, print_map


class cinema():
    def __new__(cls, title, row, col):
        """ 
        input: row max 26, col max 50, none zero
        """
        if row > 26 or col > 50 or row <= 0 or col <= 0:
            raise ValueError("parameters_out_of_bound")
        else:
            # instance = super().__new__(cls)
            instance = super(cinema, cls).__new__(cls)
            return instance

    def __init__(self, title, row, col):
        """
        Init class param and create 2D array of cinema map
        """

        self.title, self.row, self.col = title, row, col
        self.booking_id = 1
        self.create_cinema_map()

    def create_cinema_map(self):
        """
        Create 2D map for the cinema, with Dict of label( Not used) and booking 
        Note that the map is in reversed ROW order 
        """
        cinema_map = []

        for r in range(self.row):
            cinema_row = []
            for c in range(self.col):
                cinema_row.append(
                    {"row_label": chr(r+ord('A')), "col_label": str(c+1), "booking": None})
            cinema_map.append(cinema_row)

        self.cinema_map = cinema_map

    def auto_booking(self, num_ticket=4, cinema_map_preview=None, start_row=None):
        """
        Get default seat
        Param: cinema_map_preview and start_row must be define at the same time to continue for custom booking 
        Return: 2D array marked by O
        Note: Should be called by custom_booking.

        """
        if cinema_map_preview is None:
            cinema_map_preview = deepcopy(self.cinema_map)

        for r in range(self.row):
            # (optional) continue from custom booking request
            if start_row is not None and r < start_row:
                continue

            # odd col, try middle seat
            if self.col % 2 == 1:
                if self.cinema_map[r][self.col//2]["booking"] == None:
                    cinema_map_preview[r][self.col//2]["booking"] = "O"
                    num_ticket = num_ticket-1
                    if num_ticket <= 0:
                        return cinema_map_preview

            for c in reversed(range(self.col//2)):
                if self.cinema_map[r][c]["booking"] == None:
                    cinema_map_preview[r][c]["booking"] = "O"
                    num_ticket = num_ticket-1
                    if num_ticket <= 0:
                        return cinema_map_preview

                if self.cinema_map[r][self.col-c-1]["booking"] == None:
                    cinema_map_preview[r][self.col-c-1]["booking"] = "O"
                    num_ticket = num_ticket-1
                    if num_ticket <= 0:
                        return cinema_map_preview

        raise ValueError("not_enough_seat")

    def custom_booking(self, num_ticket=4, start_row=0, start_col=0):
        """
        Get default seat, without updating back.
        start_row =0, start_col=0 -> Equal to auto book
        return 2D array marked by O
        """
        cinema_map_preview = deepcopy(self.cinema_map)
        try:
            if not (start_row <= 0 and start_col <= 0):
                # book in start row
                for c in range(start_col, self.col):
                    if self.cinema_map[start_row][c]["booking"] == None:
                        cinema_map_preview[start_row][c]["booking"] = "O"
                        num_ticket = num_ticket-1
                        if num_ticket <= 0:
                            return cinema_map_preview
                start_row = start_row+1

            return (self.auto_booking(num_ticket=num_ticket, cinema_map_preview=cinema_map_preview, start_row=start_row))
        except:
            raise ValueError("booking_error")

    def save_booking(self, cinema_map_preview, booking_id):
        """
        Commit booking into cinema map ( i.e. database but in running memory)
        """
        for c in range(self.row):
            for r in range(self.col):
                if cinema_map_preview[c][r]["booking"] == "O":
                    self.cinema_map[c][r]["booking"] = booking_id
        self.booking_id = self.booking_id+1

    def get_booking(self, booking_id):
        """
        Get booking ID
        return 2D array of booking ID, marked by O
        """
        cinema_map_preview = deepcopy(self.cinema_map)
        num_seat = 0
        for c in range(self.row):
            for r in range(self.col):
                if self.cinema_map[c][r]["booking"] == booking_id:
                    cinema_map_preview[c][r]["booking"] = "O"
                    num_seat = num_seat+1
                elif self.cinema_map[c][r]["booking"] is not None:
                    cinema_map_preview[c][r]["booking"] = "#"
                else:
                    cinema_map_preview[c][r]["booking"] = None
        if (num_seat == 0):
            raise ValueError("no_booking")
        else:
            return cinema_map_preview

    def seat_available(self):
        """
        return how many seats are available ( int) 
        """
        num_seats = 0
        for c in range(self.row):
            for r in range(self.col):
                if self.cinema_map[c][r]["booking"] is None:
                    num_seats = num_seats+1
        return num_seats
