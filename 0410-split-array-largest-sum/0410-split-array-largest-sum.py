class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            parts, s = 1, 0
            for num in nums:
                if s + num > mid:
                    parts += 1
                    s = num
                else:
                    s += num
            if parts <= k:
                r = mid
            else:
                l = mid + 1
        return l