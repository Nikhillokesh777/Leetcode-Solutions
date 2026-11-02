class Solution:
    def minMoves(self, nums: list[int]) -> int:
        low = min(nums)
        return sum(nums)-len(nums)*low