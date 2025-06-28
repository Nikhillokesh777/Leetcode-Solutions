from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        temp = len(nums)//2
        return nums[temp]
             