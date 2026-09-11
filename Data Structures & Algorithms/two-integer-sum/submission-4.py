class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}   # num, idx
        for i, n in enumerate(nums):
            if target - n in diff:
                j = diff.get(target - n, -1)
                return [j, i]

            diff[n] = i
        
        return [-1, -1]