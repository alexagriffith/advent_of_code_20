
class SeatFinder(object):
    def __init__(self, input_file='input.txt'):
        self.input_file = input_file
        self.highest_id = 0

    def execute(self):
        boarding_passes = self.read_boarding_passes()
        seat_info = self.find_seat_ids(boarding_passes)
        return self.get_highest_seat_id(seat_info), self.find_your_seat(seat_info)

    def read_boarding_passes(self):
        boarding_passes = []
        f = open(self.input_file, "r")
        for line in f:
            boarding_pass = line.strip()
            boarding_passes.append(boarding_pass)
        f.close()
        return boarding_passes

    def find_seat_ids(self, boarding_passes):
        seat_info = {}
        rows = list(range(128))
        columns = list(range(8))
        for boarding_pass in boarding_passes:
            row = rows[:]
            col = columns[:]
            for char in boarding_pass:
                if char == 'F':
                    row = row[:len(row) // 2]
                if char == 'B':
                    row = row[len(row) // 2:]
                if char == 'L':
                    col = col[:len(col) // 2]
                if char == 'R':
                    col = col[len(col) // 2:]
            seat_info[boarding_pass] = dict(row=row[0], column=col[0], seat_id=row[0] * 8 + col[0])
        return seat_info

    def get_highest_seat_id(self, seat_info):
        # probably a much better way to do this to avoid the second lookup
        max_seat = max(seat_info.keys(), key=lambda k: seat_info[k]['seat_id'])
        return seat_info[max_seat]['seat_id']

    def find_your_seat(self, seat_info):
        # this feels yuck..surely I can do better.
        seat_map = self.fill_seat_map(seat_info)
        for row in seat_map:
            if row == [0] * 8:
                continue
            if 0 in row:
                open_seat = row.index(0)
                if row[open_seat - 1] and row[open_seat + 1]:
                    return row[open_seat - 1] + 1

    def fill_seat_map(self, seat_info):
        seats = [[0] * 8 for i in range(128)]
        for seat, info in seat_info.items():
            seats[info['row']][info['column']] = info['seat_id']

        return seats


# result = SeatFinder(input_file='input_test.txt').execute()
highest_seat_id, your_seat = SeatFinder().execute()
print(f"higest seat id: {highest_seat_id}, your seat: {your_seat}")
