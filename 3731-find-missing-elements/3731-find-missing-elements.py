
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        left = min(nums)
        right = max(nums)

        ans = []
        for i in range(left + 1, right):
            if i not in s:
                ans.append(i)

        return ans