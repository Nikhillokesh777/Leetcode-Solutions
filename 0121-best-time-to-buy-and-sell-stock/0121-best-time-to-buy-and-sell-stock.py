class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        ans = 0
        for p in prices:
            if p < min_val:
                min_val = p
            else:
                ans = max(ans,p-min_val)
        return ans