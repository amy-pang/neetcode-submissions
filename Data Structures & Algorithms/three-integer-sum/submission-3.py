class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, k = 0, len(nums) - 1
        j = k - 1
        res = set()
        nums.sort()
        while i < k and j < k:
            # [-1,0,1,2,-1,-4]
            # [-4, -1, -1, 0, 1, 2]
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    res.add((nums[i], nums[j], nums[k]))
                    i, j = i + 1, j - 1
                elif nums[i] + nums[j] > -nums[k]:
                    j -= 1
                else:
                    i += 1
            i, k = 0, k - 1
            j = k - 1

        return list(res)