class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        memoFirst = [0] * (len(nums) - 1)
        memoLast = [0] * (len(nums) - 1)
        memoFirst[0] = nums[0]
        memoFirst[1] = max(nums[0], nums[1])
        memoLast[0] = nums[1]
        memoLast[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            memoFirst[i] = max(memoFirst[i - 2] + nums[i], memoFirst[i - 1])
            memoLast[i] = max(memoLast[i - 2] + nums[i + 1], memoLast[i - 1])
        
        return max(memoFirst[-1], memoLast[-1])