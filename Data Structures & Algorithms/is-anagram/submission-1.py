class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        t.sort()
        s.sort()
        if s == t:
            return True
        else:
            return False