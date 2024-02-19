class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for ast in asteroids:
            collision = False
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                collision = True
                break
            if not collision:
                stack.append(ast)
        return stack