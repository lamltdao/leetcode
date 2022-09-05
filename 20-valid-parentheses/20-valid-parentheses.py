class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_c = set(['(', '{', '['])
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in open_c:
                stack.append(c)
            else: # closing brackets
                if len(stack) > 0 and pairs[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0