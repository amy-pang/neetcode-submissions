class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy from beginning
        jumps = 0
        l = r = 0
        while r < len(nums) - 1: #only need to land on last element
            farthest = 0
            # takable steps
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            jumps += 1
            l = r + 1
            r = farthest
            
        return jumps