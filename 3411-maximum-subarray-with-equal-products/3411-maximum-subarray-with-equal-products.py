from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        limit = lcm(*nums) * max(nums)
        ans = 0
        for i in range(n):
            prod, g, l = 1, 0, 1
            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if prod == g * l:
                    ans = max(ans, j - i + 1)
                if prod > limit:
                    break
        return ans