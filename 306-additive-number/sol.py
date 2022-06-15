class Solution:
    def check_leading_zero(self, num, from_idx, to_idx):
        return not (num[from_idx+1] == '0' and from_idx + 1 < to_idx)
    def check_sum(self, num, idx1, idx2, idx3, idx4):
        return int(num[idx1+1:idx2+1]) + int(num[idx2+1:idx3+1]) == int(num[idx3+1:idx4+1])
    def bt(self, indices, num, ans):
        if ans[0]:
            return
        last = indices[-1]
        if last == len(num)-1:
            if len(indices) > 2:
                # print(indices)
                ans[0] = True
            return
        last = indices[-1]
        prev_last = indices[-2]
        prev_prev_last = indices[-3] if len(indices) > 2 else -1
        for i in range(last+1, len(num)):
            if self.check_leading_zero(num, last, i) and self.check_sum(num, prev_prev_last, prev_last, last, i):
                indices.append(i)
                self.bt(indices, num, ans)
                indices.pop()
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <= 2:
            return False
        ans = [False]
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if self.check_leading_zero(num,-1,i) and self.check_leading_zero(num, i, j):
                    self.bt([i,j], num, ans)
        return ans[0]
