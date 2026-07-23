class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]

        while l < r:
            mid = (l + r + 1) // 2

            balls = 1
            last = position[0]

            for x in position[1:]:
                if x - last >= mid:
                    balls += 1
                    last = x

            if balls >= m:
                l = mid
            else:
                r = mid - 1

        return l
