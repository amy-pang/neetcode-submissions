class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water_trapped = 0

        while l < r:
            if max_l < max_r:
                water_trapped += max(max_l - height[l], 0)
                l += 1
                max_l = max(max_l, height[l])
            else:
                water_trapped += max(max_r - height[r], 0)
                r -=1
                max_r = max(max_r, height[r])

        return water_trapped

            