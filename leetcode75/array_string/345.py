class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        vowel_list = [char for char in s if char in vowels]  # 입력 문자열에서 모음만 추출
        reversed_vowels = vowel_list[::-1]  # 모음 리스트를 역순으로 뒤집음
        
        # 원래 문자열에서 모음은 0으로 대체하고 자음은 그대로 유지하는 리스트 생성
        masked_list = [char if char not in vowels else 0 for char in s]
        
        # masked_list에서 0을 역순으로 된 모음으로 대체
        reversed_vowel_index = 0
        for i in range(len(masked_list)):
            if masked_list[i] == 0:
                masked_list[i] = reversed_vowels[reversed_vowel_index]
                reversed_vowel_index += 1
        
        # 리스트를 다시 문자열로 변환
        return ''.join(masked_list)        