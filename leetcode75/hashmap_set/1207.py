from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        # 배열에서 각 숫자의 등장 횟수를 카운트합니다.
        nums_counter = Counter(arr)
        
        # 등장 횟수만을 담은 리스트를 생성합니다.
        occurrences = list(nums_counter.values())
        
        # 등장 횟수의 리스트를 set으로 변환하여 중복을 제거합니다.
        unique_occurrences = set(occurrences)
        
        # 원래 리스트와 set 변환된 리스트의 길이가 동일하면 True, 아니면 False를 반환합니다.
        return len(occurrences) == len(unique_occurrences)
