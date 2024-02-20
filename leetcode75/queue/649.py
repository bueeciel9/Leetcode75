class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = deque()
        dire = deque()
        
        # 각 당의 상원의원들을 큐에 추가
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # 두 당 모두 상원의원이 남아있는 동안 반복
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            
            # 먼저 행동할 수 있는 상원의원이 반대 당의 상원의원의 권리를 박탈
            if r < d:
                radiant.append(r + len(senate))  # 다음 라운드로 이동
            else:
                dire.append(d + len(senate))  # 다음 라운드로 이동
        
        # 남아 있는 당에 따라 승리 당을 반환
        return "Radiant" if radiant else "Dire"
    
    
    class Solution:
        def predictPartyVictory(self, senate):
            q = deque(senate)
            radiant, dire = 0, 0

            while q:
                s = q.popleft()
                if s == 'R':
                    if dire > 0:
                        dire -= 1
                    else:
                        radiant += 1
                        q.append(s)
                else:  # s == 'D'
                    if radiant > 0:
                        radiant -= 1
                    else:
                        dire += 1
                        q.append(s)

                if not radiant or not dire:
                    return "Radiant" if radiant else "Dire"
            