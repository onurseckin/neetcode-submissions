class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for n in range(len(s)-1):
            res += abs(ord(s[n]) - ord(s[n+1]))

        return res