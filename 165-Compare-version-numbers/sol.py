class Solution:
    def getNextNum(self, s:str, from_idx: int) -> int:
        num = ''
        while from_idx < len(s) and s[from_idx] != '.':
            num += s[from_idx]
            from_idx += 1
        return (0 if num == '' else int(num), from_idx+1)
    def compareVersion(self, version1: str, version2: str) -> int:
        ptr1 = ptr2 = 0
        while ptr1 < len(version1) or ptr2 < len(version2):
            n1, next_1 = self.getNextNum(version1, ptr1)
            n2, next_2 = self.getNextNum(version2, ptr2)
            if n1 != n2:
                return 1 if n1 > n2 else -1
            else:
                ptr1 = next_1
                ptr2 = next_2
        return 0
