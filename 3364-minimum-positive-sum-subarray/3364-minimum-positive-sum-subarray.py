class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for size in range(l, r + 1):
            window_sum = sum(nums[:size])

            if window_sum > 0:
                ans = min(ans, window_sum)

            for i in range(size, len(nums)):
                window_sum += nums[i]
                window_sum -= nums[i - size]

                if window_sum > 0:
                    ans = min(ans, window_sum)

        return ans if ans != float('inf') else -1