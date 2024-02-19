from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        # 두 문자열의 고유 문자 집합이 동일한지 검사
        if set(word1) != set(word2):
            return False
        
        # 두 문자열에서 각 문자의 등장 횟수를 카운트
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        # 두 문자열에서 각 문자의 등장 횟수 집합이 동일한지 검사
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        
        return True
