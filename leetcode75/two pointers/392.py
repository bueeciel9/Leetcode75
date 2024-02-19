class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index =0
        t_index =0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1  # s의 다음 문자로 이동합니다.
            t_index += 1  # t의 다음 문자로 이동합니다.

        return s_index == len(s)  # s의 모든 문자를 찾았는지 확인합니다.