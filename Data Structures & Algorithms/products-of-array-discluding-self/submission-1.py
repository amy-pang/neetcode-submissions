class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[i] = suffix[i - 1] * nums[-i]
        print(prefix, suffix)
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = prefix[i] * suffix[-(i + 1)]
        
        return res