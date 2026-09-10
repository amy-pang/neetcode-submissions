class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in vals:
                return [vals[diff], i]
            vals[n] = i
        
        return [-1, -1]
