class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        count = 0

        # Step 1: Skip any spaces at the very end of the string
        while p >= 0 and s[p] == " ":
            p -= 1

        # Step 2: Count characters until we hit a space or start of string
        while p >= 0 and s[p] != " ":
            count += 1
            p -= 1

        return count