class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bt(num_l, tmp):
            nonlocal n, ans
            if len(tmp) == 2*n:
                ans.append(''.join(tmp))
                return
            if num_l < n:
                tmp.append('(')
                bt(num_l+1, tmp)
                tmp.pop()
            if num_l > 0 and num_l * 2 > len(tmp):
                tmp.append(')')
                bt(num_l, tmp)
                tmp.pop()
        bt(0, [])
        return ans