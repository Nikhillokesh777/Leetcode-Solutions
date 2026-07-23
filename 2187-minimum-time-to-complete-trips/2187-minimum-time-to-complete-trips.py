class Solution:
    def minimumTime(self, time, totalTrips):
        l = 1
        r = min(time) * totalTrips
        while l < r:
            m = (l + r) // 2
            trips = 0
            for t in time:
                trips += m // t
            if trips >= totalTrips:
                r = m
            else:
                l = m + 1
        return l