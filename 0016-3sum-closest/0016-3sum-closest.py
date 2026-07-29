from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        min_sum = nums[0] + nums[1] + nums[2]
        if min_sum >= target:
            return min_sum


        max_sum = nums[-1] + nums[-2] + nums[-3]
        if max_sum <= target:
            return max_sum

        closest = min_sum
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target  # Exact match

        return closest