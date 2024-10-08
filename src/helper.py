from jinja2 import Environment, select_autoescape, FileSystemLoader
import pathlib
import re


def render_template(template, **context):
    """
    Helper to render j2
    """
    env = Environment(
        loader=FileSystemLoader(pathlib.Path(
            __file__).parent.resolve() / "templates"),
        autoescape=select_autoescape()
    )

    template = env.get_template(template)
    return (template.render(context))


def print_map(cinema, map_mode=1, selected=None, booking_id=None):
    """
    Print seat map  
    Mode 1: Taken Seat -> #, ( MUST define ) Selected Seat -> O  
    Mode 2: Taken Seat -> #, (optional) same Booking ID -> O
    """
    return (render_template("map.j2", map_mode=map_mode, booking_id=booking_id,
                            row=cinema.row, col=cinema.col, cinema_map=cinema.cinema_map, selected=selected))


# def print_all (cinema, acton_mode=0, map_mode=1, **context):
#     """
#     action_mode:
#     0) Define cinema ( and then init the class, invalid option)
#     1) Main Menu
#     2) Book (auto) Ticket -> 3) Customize ticket (optional) -> 4) Accept ticket -> 5) Checking Booking
#     99) exit

#     Map Mode:
#     Mode 0: No display
#     Mode 1: Taken Seat -> #
#     Mode 2: Taken Seat -> #, Selected Seat -> O
#     """

#     context.update({ "acton_mode":acton_mode, "map_mode":map_mode,
#                     "row":cinema.row, "col":cinema.col, "title":cinema.title, "booking_id":cinema.booking_id, "num_seats":cinema.seat_available(),
#                     "cinema_map":cinema.cinema_map
#     })
#     return ( render_template("all.j2",**context))

def print_menu(cinema, action_mode=1):
    """
    Print seat map  
    Mode 1: Taken Seat -> #  
    Mode 2: Taken Seat -> #, Selected Seat -> O
    """
    return (render_template("menu.j2", action_mode=action_mode, num_seats=cinema.seat_available(), title=cinema.title))


# def get_valid_input(str_prompt, valid_answer=[]):
#     while True:
#         ans = input(str_prompt)
#         if ans in valid_answer:
#             return (ans)


def seat_id_from_label(seat_label=""):
    """
    E.g Convert B03 -> (1, 2)
    """

    if re.search('^[A-Z]\\d+$', seat_label):
        row = ord(seat_label[:1])-ord("A")
        col = int(seat_label[1:])-1
        return (row, col)


def seat_label_from_id(row, col):
    """
    E.g Convert ( 1,1)  => B2
    """
    return ("{}{}".format(chr(row+ord('A')), str(col+1)))


def mock_seat_map(seat_map, row, col, booking_id, seats=()):
    """
    Mock booking by updating seat map manually
    """
    for r in range(row):
        for c in range(col):
            # print (seat_label_from_id(r, c))
            if seat_label_from_id(r, c) in seats:
                # print (r, c)
                seat_map[r][c]["booking"] = booking_id
