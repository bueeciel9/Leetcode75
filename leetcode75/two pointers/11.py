class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_index = 0
        end_index = len(height)-1
        max_area =0
        current_area =0

        while start_index<end_index:
            if height[start_index] >= height[end_index]:
                current_area = height[end_index]*(end_index-start_index)
                end_index -=1
                if current_area>max_area:
                    max_area = current_area
            else:
                current_area = height[start_index]*(end_index-start_index)
                start_index +=1
                if current_area>max_area:
                    max_area = current_area
                    
        return max_area