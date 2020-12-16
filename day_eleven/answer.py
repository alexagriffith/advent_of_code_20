import itertools as it


class SeatingSystem(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def execute(self):
        seats = self.read_input()
        num_occupied = self.stabilize_seats(seats)
        return num_occupied

    def read_input(self):
        seats = []
        f = open(self.input_file, "r")
        for line in f:
            seats.append([[seat, 0 if seat == 'L' else None]
                          for seat in line.strip()])
        return seats

    def stabilize_seats(self, seats):
        seats_changed = True
        updated_status_seats = []
        while seats_changed:
            updated_score_seats = self.score_seats(seats)
            updated_status_seats, seats_changed = self.update_seating(updated_score_seats)

        num_occupied = sum([list(it.chain(*row)).count('#') for row in updated_status_seats])
        return num_occupied

    def score_seats(self, seats):
        for row_idx, seat_row in enumerate(seats):
            for seat_idx, seat in enumerate(seat_row):
                seat_coords = (row_idx, seat_idx)
                if seats[row_idx][seat_idx][0] != '.':
                    x, y = self.find_adjacent_coords(row_idx, seat_idx, len(seats), len(seat_row))
                    adjacent_coords = list(it.product(y, x))
                    adjacent_coords.remove(seat_coords)

                    seat_score = [seats[coord[0]][coord[1]][0] for coord in adjacent_coords].count('#')
                    seats[row_idx][seat_idx][1] = seat_score
        return seats

    def find_adjacent_coords(self, row_idx, seat_idx, row_len, seat_len):
        first_row = row_idx == 0
        last_row = row_idx ==  row_len - 1
        first_seat = seat_idx == 0
        last_seat = seat_idx == seat_len - 1
        if first_row:
            y = (row_idx, row_idx + 1)
        elif last_row:
            y = (row_idx, row_idx - 1)
        else:
            y = (row_idx - 1, row_idx, row_idx + 1)

        if first_seat:
            x = (seat_idx, seat_idx + 1)
        elif last_seat:
            x = (seat_idx, seat_idx - 1)
        else:
            x = (seat_idx - 1, seat_idx, seat_idx + 1)

        return x, y

    def update_seating(self, seats):
        seat_row = 0
        seat_num = 0
        has_changed = False
        while seat_row < len(seats) and seat_num < len(seats[0]):
            seat = seats[seat_row][seat_num]
            if seat[0] == '.':
                pass
            else:
                if seat[1] == 0 and seat[0] == 'L':
                    seat[0] = '#'
                    has_changed = True
                elif seat[1] >= 4 and seat[0] == '#':
                    seat[0] = 'L'
                    has_changed = True

            if seat_num == len(seats[0]) - 1:
                seat_num = 0
                seat_row += 1
            else:
                seat_num += 1
        return seats, has_changed


result = SeatingSystem(input_file='input.txt').execute()
print(result)
