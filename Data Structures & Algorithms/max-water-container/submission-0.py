class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0 
        right = len(heights) - 1

        while left < right:
            distance = right - left
            if heights[right] >= heights[left]:
                low = heights[left]
                left +=1
            else:
                low = heights[right]
                right -=1
           
            volume = distance * low
            result = max(volume, result)


        return result
            
        