
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        ans = 0
        count = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
                ans += count
            else:
                count = 0

        return ans
