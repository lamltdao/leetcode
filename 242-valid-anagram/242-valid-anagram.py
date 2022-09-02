class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alps = [0 for _ in range(26)]
        for i in range(len(s)):
            alps[ord(s[i]) - ord('a')] += 1
            alps[ord(t[i]) - ord('a')] -= 1
        for count in alps:
            if count != 0:
                return False
        return True