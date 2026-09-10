class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1 3 2 0 1
        # go backwards
        i = len(nums) - 1
        while i > 0:
            j = i - 1
            while j > -1:
                if nums[j] >= (i - j):
                    i = j
                    break
                j -= 1
            if j == -1:
                print(i, j)
                return False
        return True