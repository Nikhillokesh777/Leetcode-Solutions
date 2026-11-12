class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 0
        dec = 0
        ans = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 0

            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 0

            else:
                inc = 0
                dec = 0

            ans = max(ans, inc + 1, dec + 1)

        return ans