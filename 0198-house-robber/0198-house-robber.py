# class Solution:
#     def rob(self, nums):
#         if len(nums) == 1:
#             return nums[0]

#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

#         return dp[-1]



class Solution:
    def rob(self, nums):
        prev2, prev1 = 0, 0  

        for i in nums:
            curr = max(prev2 + i, prev1)
            prev2, prev1 = prev1, curr

        return prev1

