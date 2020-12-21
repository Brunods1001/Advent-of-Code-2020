import sys

from soln1 import get_id, get_seat

try:
    fname = sys.argv[1]
except IndexError:
    fname = 'input.txt'

with open(fname, 'r') as f:
    list_seats = f.read().split('\n')

# the seats with IDs += 1 from yours will be on your list

taken_seats = list(range(8))
for seat in list_seats:
    row, column = get_seat(seat)
    seat_id = get_id(row, column)
    taken_seats.append(seat_id)
id_max = max(taken_seats)
taken_seats += list(range(id_max + 1, id_max + 9))

taken_seats = sorted(taken_seats)

possible_seats = []
for i in range(1, len(taken_seats) - 1):
    s0 = taken_seats[i - 1]
    s1 = taken_seats[i]
    s2 = taken_seats[i + 1]
    if s0 + 1 != s1:
        possible_seats.append(s1 - 1)
    if s1 != s2 - 1:
        possible_seats.append(s1 + 1)

set_seats = set([])
for i in possible_seats:
    if possible_seats.count(i) > 1:
        set_seats.add(i)

print('Your seat could be:', set_seats)
