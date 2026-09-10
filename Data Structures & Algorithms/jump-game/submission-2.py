class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1 3 2 0 1
        # go backwards
        goalIdx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] + i) >= goalIdx:
                goalIdx = i
        return goalIdx == 0