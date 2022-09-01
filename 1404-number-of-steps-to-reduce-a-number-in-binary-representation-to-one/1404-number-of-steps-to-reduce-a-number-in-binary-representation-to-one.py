class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        s = deque(list(s))
        while not (len(s) == 1 and s[0] == '1'):
            step += 1
            if s[-1] == '0':
                s.pop()
            else:
                tmp = len(s)-1
                carry = 1
                while tmp >= 0 and carry:
                    if s[tmp] == '0':
                        s[tmp] = '1'
                        carry = 0
                    else:
                        s[tmp] = '0'
                    tmp -= 1
                if carry: # case 1111 + 1
                    s.appendleft("1")
        return step
