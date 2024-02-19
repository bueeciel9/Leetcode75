class Solution(object):
    def removeStars(self, s):
        stack = []  # 문자를 저장할 리스트(스택)를 사용

        for char in s:
            if char == "*":
                stack.pop()  # 스택에서 마지막 문자 제거
            else:
                stack.append(char)  # 스택에 문자 추가
        
        # 스택에 남아 있는 문자들을 문자열로 합쳐서 반환
        return ''.join(stack)
