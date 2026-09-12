class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            height = min(heights[l], heights[r])
            water_area = (r - l) * height
            max_water = max(max_water, water_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_water
