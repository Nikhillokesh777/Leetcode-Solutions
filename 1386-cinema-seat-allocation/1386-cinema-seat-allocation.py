class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        result = (n - len(reserved)) * 2

        for seats in reserved.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            left_available = seats.isdisjoint(left)
            middle_available = seats.isdisjoint(middle)
            right_available = seats.isdisjoint(right)

            if left_available and right_available:
                result += 2

            elif left_available or middle_available or right_available:
                result += 1

        return result