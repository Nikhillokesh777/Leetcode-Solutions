from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max1 = 0
        for j in range(n-1, -1, -1):
            if colors[j] != colors[0]:
                max1 = j
                break
        max2 = 0
        for i in range(n):
            if colors[i] != colors[n-1]:
                max2 = n - 1 - i
                break
        
        return max(max1, max2)
