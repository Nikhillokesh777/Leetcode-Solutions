class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            d = 1      # days used
            load = 0   # current ship load
            for weight in weights:
                if load + weight <= mid:
                    load +=weight
                else:
                    d += 1
                    load =weight
            if d <= days:
                right = mid
            else:
                left = mid + 1

        return left