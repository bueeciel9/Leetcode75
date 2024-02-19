class Solution(object):



    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def find_common_divisors(a, b):
            common_divisors = []  # 공약수를 저장할 리스트
            for i in range(1, min(a, b) + 1):
                if a % i == 0 and b % i == 0:
                    common_divisors.append(i)
            common_divisors.sort(reverse=True)
            return common_divisors

        common_divisors = find_common_divisors(len(str1), len(str2))
        
        # 최대공약수 길이의 문자열이 두 문자열에서 반복되는지 확인
        for i in range(len(common_divisors)):
            candidate = str1[:common_divisors[i]]
            if str1 == candidate * (len(str1) // common_divisors[i]) and str2 == candidate * (len(str2) // common_divisors[i]):
                return candidate
            else:
                return ""
        
