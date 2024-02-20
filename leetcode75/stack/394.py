class Solution(object):
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == '[':
                # 현재 문자열과 반복 횟수를 스택에 저장
                stack.append((curString, curNum))
                # 초기화
                curString = ''
                curNum = 0
            elif c == ']':
                # 스택에서 문자열과 반복 횟수를 팝
                prevString, num = stack.pop()
                # 현재 문자열을 반복하고 이전 문자열에 이어붙임
                curString = prevString + num * curString
            else:
                curString += c
        return curString