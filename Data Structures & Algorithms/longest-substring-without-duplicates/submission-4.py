class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        letters = {}
        start = 0
        for i in range(len(s)):
            if s[i] in letters and letters[s[i]] >= start:
                start = letters[s[i]] + 1
            letters[s[i]] = i
            best = max(best, i - start + 1)
        return best