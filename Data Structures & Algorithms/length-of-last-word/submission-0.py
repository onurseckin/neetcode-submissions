class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        p = n-1
        count = 0

        for i in range(n-1, -1, -1):
            if s[i] == " ":
                p -= 1
            else:
                break

        for i in range(p, -1, -1):
            if s[i] != " ":
                count +=1
            else:
                break

        
        return count

