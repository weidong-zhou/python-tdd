from cinema import cinema
from helper import *
import sys
import re


class booking_flow ():

    def main(self):
        self.get_cinema_params()
        while True:
            # opt=get_valid_input("Get from J2", ["1","2","3"])
            opt = input(print_menu(self.cinema))
            if opt == "1":
                self.new_booking()
            elif opt == "2":
                self.get_booking()
            elif opt == "3":
                break

    def get_cinema_params(self):
        title, row, col = ["", 0, 0]
        while True:
            ans = input(
                "Please define movie title and seating map in [Title] [Row] [SeatPerRow] format\n>")
            arr = ans.split(" ")
            if len(arr) >= 3 and \
                (arr[-1].isnumeric() and int(arr[-1]) > 0 and int(arr[-1]) <= 26) and \
                    (arr[-2].isnumeric() and int(arr[-2]) > 0 and int(arr[-2]) <= 50):
                title = "".join(arr[0:-2])
                row = int(arr[-2])
                col = int(arr[-1])
                break
        self.title, self.row, self.col = (title, row, col)
        self.cinema = cinema(title=title, row=row, col=col)

    def new_booking(self):
        booking_id = self.cinema.booking_id
        available_seat = self.cinema.seat_available()

        while True:
            ans = input(
                "Enter number of tickets to book, or enter blank to go back to main menu\n>")
            if re.search('^\\d+$', ans):
                self.num_ticket = int(ans)
                if self.num_ticket > available_seat:
                    print("Sorry, there are only {} seats available".format(
                        available_seat))
                    continue
                print("Sucessfully reserved {} tickets".format(self.cinema.title))
                print("Booking id: GIC{:04d}".format(booking_id))
                print("Selected Seats:")
                # try:
                self.booking_map = self.cinema.custom_booking(
                    num_ticket=self.num_ticket)
                # except ValueError:
                #     print("Sorry, there are only {} seats available".format(
                #         available_seat))
                # break
                # except Exception as err:
                #     print(f"Unexpected {err=}, {type(err)=}")
                #     break

                print(print_map(self.cinema, map_mode=1, selected=self.booking_map))
                self.review_booking()
                break
            elif re.search('^\\s*$', ans):
                print("return to main")
                break

    def review_booking(self):
        booking_id = self.cinema.booking_id
        available_seat = self.cinema.seat_available()

        while True:
            ans = input(
                "Enter blank to accept seat selection, or enter new seating position\n>")
            if re.search('^\\s*$', ans):  # blank to save and exit
                self.cinema.save_booking(
                    cinema_map_preview=self.booking_map, booking_id=booking_id)
                print("Booking id: GIC{:04d} confirmed".format(booking_id))
                break
            elif re.search('^[A-Z]\\d+$', ans):  # ask new starting seat, and loop
                # convert B03 -> 1, 2
                row = ord(ans[:1])-ord("A")
                col = int(ans[1:])-1
                try:
                    self.booking_map = self.cinema.custom_booking(
                        num_ticket=self.num_ticket, start_row=row, start_col=col)
                except ValueError:
                    print("Sorry, there are only {} seats available".format(
                        available_seat))
                    break
                # except Exception as err:
                #     print(f"Unexpected {err=}, {type(err)=}")
                #     break
                print("Sucessfully reserved {} tickets".format(self.cinema.title))
                print("Booking id: GIC{:04d}".format(booking_id))
                print("Selected Seats:")
                print(print_map(self.cinema, map_mode=1, selected=self.booking_map))
                self.review_booking()
                break

    def get_booking(self):
        booking_id = self.cinema.booking_id
        while True:
            ans = input(
                "Enter booking id or enter blank to go back to main menu\n>")
            if re.search('^\\s*$', ans):
                break
            elif re.search('^GIC[\\d]+$', ans):
                booking_id = int(ans[4:])
                print(ans[3:])
                # print ( "{}{}".format(row , col) )
                try:
                    self.booking_map = self.cinema.get_booking(
                        booking_id=booking_id)
                except ValueError:
                    print("Error find booking ID!")
                    break
                # except Exception as err:
                #     print(f"Unexpected {err=}, {type(err)=}")
                #     break
                print("Booking id: GIC{:04d}".format(booking_id))
                print("Selected Seats:")
                print(print_map(self.cinema, map_mode=1, selected=self.booking_map))
