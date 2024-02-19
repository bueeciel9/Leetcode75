class Solution(object):
    def findDifference(self, nums1, nums2):
        # nums1과 nums2를 집합으로 변환
        set1 = set(nums1)
        set2 = set(nums2)
        
        # nums1에만 있는 고유한 요소 찾기
        diff1 = list(set1 - set2)
        
        # nums2에만 있는 고유한 요소 찾기
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]
