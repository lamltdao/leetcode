class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        res = []
        cnt = 0
        while a_idx >= 0 and b_idx >= 0:
            if a[a_idx] == '1':
                if b[b_idx] == '1':
                    if cnt == 0:
                        res.append('0')
                    else:
                        res.append('1')
                    cnt = 1
                else:
                    if cnt == 0:
                        res.append('1')
                    else:
                        res.append('0')
            else:
                if b[b_idx] == '1':
                    if cnt == 0:
                        res.append('1')
                    else:
                        res.append('0')
                else:
                    if cnt == 0:
                        res.append('0')
                    else:
                        res.append('1')
                        cnt = 0
            a_idx -= 1
            b_idx -= 1
        while a_idx >= 0:
            if cnt == 0:
                res.append(a[a_idx])
            else:
                if a[a_idx] == '1':
                    res.append('0')
                else:
                    res.append('1')
                    cnt = 0
            a_idx -= 1
        while b_idx >= 0:
            if cnt == 0:
                res.append(b[b_idx])
            else:
                if b[b_idx] == '1':
                    res.append('0')
                else:
                    res.append('1')
                    cnt = 0
            b_idx -= 1
        if cnt == 1:
            res.append('1')
        return ''.join(res[::-1])
                