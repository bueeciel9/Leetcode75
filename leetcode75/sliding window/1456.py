class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        max_vowels = 0
        current_vowels = 0

        # 처음 k 길이의 윈도우 내 모음 수 계산
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        # 슬라이딩 윈도우로 나머지 문자열 탐색
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i-k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
