from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        l = 0
        temp = 0
        ans = -1

        for r in range(len(nums)):
            temp += nums[r]

            while temp > target:
                temp -= nums[l]
                l += 1
            if temp == target:
                ans = max(ans, r - l + 1)
        if ans == -1:
            return -1

        return len(nums)-ans