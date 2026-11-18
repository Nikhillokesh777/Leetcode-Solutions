class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        temp=0
        ans = float("inf")
        for right in range(len(nums)):
            temp+=nums[right]
            while temp>=target:
                ans =min(ans,right-left+1)
                temp-=nums[left]
                left+=1
        if ans == float("inf"):
            return 0
        return ans

