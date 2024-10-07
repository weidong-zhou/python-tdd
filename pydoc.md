<a id="booking_flow"></a>

# booking\_flow

<a id="booking_flow.booking_flow"></a>

## booking\_flow Objects

```python
class booking_flow()
```

<a id="booking_flow.booking_flow.main"></a>

#### main

```python
def main()
```

Main entry point

<a id="booking_flow.booking_flow.get_cinema_params"></a>

#### get\_cinema\_params

```python
def get_cinema_params()
```

Get input for cinema parameters

<a id="booking_flow.booking_flow.new_booking"></a>

#### new\_booking

```python
def new_booking()
```

Handle new booking request

<a id="booking_flow.booking_flow.review_booking"></a>

#### review\_booking

```python
def review_booking()
```

Review and save booking, allow different starting seat postion

<a id="booking_flow.booking_flow.get_booking"></a>

#### get\_booking

```python
def get_booking()
```

Display booking

<a id="__init__"></a>

# \_\_init\_\_

<a id="helper"></a>

# helper

<a id="helper.render_template"></a>

#### render\_template

```python
def render_template(template, **context)
```

Helper for render j2

<a id="helper.print_map"></a>

#### print\_map

```python
def print_map(cinema, map_mode=1, selected=None, booking_id=None)
```

Print seat map
Mode 1: Taken Seat -> #, ( MUST define ) Selected Seat -> O
Mode 2: Taken Seat -> #, (optional) same Booking ID -> O

<a id="helper.print_menu"></a>

#### print\_menu

```python
def print_menu(cinema, action_mode=1)
```

Print seat map
Mode 1: Taken Seat -> #
Mode 2: Taken Seat -> #, Selected Seat -> O

<a id="helper.seat_id_from_label"></a>

#### seat\_id\_from\_label

```python
def seat_id_from_label(seat_label="")
```

Convert B03 -> (1, 2)

<a id="helper.seat_label_from_id"></a>

#### seat\_label\_from\_id

```python
def seat_label_from_id(row, col)
```

Convert ( 1,1)  => B2

<a id="helper.mock_seat_map"></a>

#### mock\_seat\_map

```python
def mock_seat_map(seat_map, row, col, booking_id, seats=())
```

Mock booking by updating seat map manually

<a id="cinema"></a>

# cinema

<a id="cinema.cinema"></a>

## cinema Objects

```python
class cinema()
```

<a id="cinema.cinema.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, title, row, col)
```

input: row max 26, col max 50, none zero

<a id="cinema.cinema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(title, row, col)
```

Init class param and create 2D array of cinema map

<a id="cinema.cinema.create_cinema_map"></a>

#### create\_cinema\_map

```python
def create_cinema_map()
```

Create 2D map for the cinema, with Dict of label( Not used) and booking 
Note that the map is in reversed ROW order

<a id="cinema.cinema.auto_booking"></a>

#### auto\_booking

```python
def auto_booking(num_ticket=4, cinema_map_preview=None, start_row=None)
```

Get default seat
Param: cinema_map_preview and start_row must be define at the same time to continue for custom booking
Return: 2D array marked by O
Note: Should be called by custom_booking.

<a id="cinema.cinema.custom_booking"></a>

#### custom\_booking

```python
def custom_booking(num_ticket=4, start_row=0, start_col=0)
```

Get default seat, without updating back.
start_row =0, start_col=0 -> Equal to auto book
return 2D array marked by O

<a id="cinema.cinema.save_booking"></a>

#### save\_booking

```python
def save_booking(cinema_map_preview, booking_id)
```

Commit booking into cinema map ( i.e. database but in running memory)

<a id="cinema.cinema.get_booking"></a>

#### get\_booking

```python
def get_booking(booking_id)
```

Get booking ID
return 2D array of booking ID, marked by O

<a id="cinema.cinema.seat_available"></a>

#### seat\_available

```python
def seat_available()
```

return how many seats are available ( int)

