import sys

try:
    fname = sys.argv[1]
except IndexError:
    fname = 'input.txt'

with open(fname, 'r') as f:
    list_seats = f.read().split('\n')


def get_seat(seat, verbose=False):
    if verbose:
        print('Finding id for', seat)
    row0, col0 = 0, 0
    rowf, colf = 127, 7
    for i in seat:
        if i == 'F':
            dr = rowf - row0
            rowf = row0 + dr // 2
        elif i == 'B':
            dr = rowf - row0
            row0 = rowf - dr // 2
        elif i == 'L':
            dc = colf - col0
            colf = col0 + dc // 2
        elif i == 'R':
            dc = colf - col0
            col0 = colf - dc // 2
        else:
            if verbose:
                print('Character not recognized')
        if verbose:
            print('Row range:', row0, rowf)
            print('Col range:', col0, colf)

    return row0, col0


def get_id(row, col):
    return row * 8 + col


max_id = 0
for seat in list_seats:
    row, column = get_seat(seat)
    seat_id = get_id(row, column)
    if seat_id > max_id:
        max_id = seat_id

print('Max id', max_id)
