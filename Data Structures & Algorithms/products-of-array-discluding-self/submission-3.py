class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1]
        suffix = [1]
        NUMS_LEN = len(nums)
        for i in range(1, NUMS_LEN):
            prefix.append(nums[i - 1] * prefix[i - 1])
            suffix.append(nums[NUMS_LEN - i] * suffix[i - 1])
        
        for i in range(NUMS_LEN):
            output.append(prefix[i] * suffix[NUMS_LEN - 1 - i])
        return output