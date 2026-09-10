class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = len(nums) - 1
        i, j = 0, k - 1
        res = []
        nums.sort()
        while i < k and j < k:
            # [-1,0,1,2,-1,-4,-2,-3,3,0,4]
            # [-4,-3,-2,-1,-1,0,0,1,2,3,4]
            while (k < len(nums) - 1) and (k > 0) and (nums[k] == nums[k + 1]):
                k -= 1
            i, j = 0, k - 1

            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    res.append((nums[i], nums[j], nums[k]))
                    i, j = i + 1, j - 1
                    while j > i and nums[j] == nums[j + 1]:
                        j -= 1
                elif nums[i] + nums[j] > -nums[k]:
                    j -= 1
                else:
                    i += 1
            k -=1

        return res