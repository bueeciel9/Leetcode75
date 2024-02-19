class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        highest =0
        current =0

        for i in range(len(gain)):
            current = current + gain[i]
            highest = max(highest, current)

        return highest