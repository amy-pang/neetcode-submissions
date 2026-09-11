class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        NUMS_LEN = len(nums)
        #prefix pass
        for i in range(1, NUMS_LEN):
            output.append(nums[i - 1] * output[-1])
        
        # suffix pass
        postfix = 1
        for i in range(NUMS_LEN - 2, -1, -1):
            postfix *= nums[i + 1]
            output[i] *= postfix
        return output