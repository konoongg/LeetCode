class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False
        s, goal = [*s], [*goal] 
        for i in range(len(s)):
            a = s[0]
            s.pop(0); s.append(a)
            if s == goal:
                return True
        return False
