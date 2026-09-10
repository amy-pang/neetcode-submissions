class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        
        for l, a in enumerate(nums):
            if a > 0:
                break

            if l > 0 and a == nums[l - 1]:
                continue

            m = l + 1
            r = len(nums) - 1
            while m < r:
                total = a + nums[m] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    res.append([a, nums[m] , nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1

        return res