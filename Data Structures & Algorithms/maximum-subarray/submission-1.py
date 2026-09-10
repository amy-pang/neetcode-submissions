class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        memo[0] = nums[0]
        maxSum = memo[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], nums[i] + memo[i - 1])
            maxSum = max(memo[i], maxSum)

        return maxSum