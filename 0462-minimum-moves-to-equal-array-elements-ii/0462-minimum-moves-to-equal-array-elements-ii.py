class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        count =0
        for val in nums:
            if val > nums[mid]:
                count+=val-nums[mid]
            else:
                count+=nums[mid]-val
        return count
        