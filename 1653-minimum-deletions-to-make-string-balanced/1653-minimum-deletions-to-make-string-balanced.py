class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        b cannot precede a
        
        every idx:
            num b before it
            num a after it
        => ans = min(min(num_b[i] + num_a[i])) for i in range(len(s))
        """
        num_a = [0 for _ in s] # num_a[i]: # of a after i
        num_b = [0 for _ in s] # num_b[i]: # of b before i
        for i in range(1, len(s)):
            num_b[i] = num_b[i-1]
            if s[i-1] == "b":
                num_b[i] += 1
        for i in range(len(s)-2, -1, -1):
            num_a[i] = num_a[i+1]
            if s[i+1] == "a":
                num_a[i] += 1
        ans = 10**5+1
        for i in range(len(s)):
            ans = min(ans, num_b[i] + num_a[i])
        return ans
        