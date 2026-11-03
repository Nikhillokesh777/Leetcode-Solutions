class Solution:
    def minMoves(self, nums: List[int]) -> int:
        val = max(nums)
        count=0
        for i in nums:
            if i <val:
                count+= val-i
        return count