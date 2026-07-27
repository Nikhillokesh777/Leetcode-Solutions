class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        s = set()   
        p = set()   
        for num in nums:
            if num - k in s:
                p.add((num - k, num))
            if num + k in s:
                p.add((num, num + k))
            s.add(num)

        return len(p)