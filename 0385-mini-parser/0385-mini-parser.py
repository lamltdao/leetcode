# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        digits = set([str(i) for i in range(10)])
        digits.add('-')
        # return idx of ] parsed
        def parse_list(s, cur_idx, ans):
            i = cur_idx
            while i < len(s):
                c = s[i]
                if c in digits:
                    num = [c]
                    while i+1 < len(s) and s[i+1] in digits:
                        i += 1
                        num.append(s[i])
                    ans.add(NestedInteger(int(''.join(num))))
                elif c == '[':
                    nested_list = NestedInteger()
                    i = parse_list(s, i+1, nested_list)
                    ans.add(nested_list)
                elif c == ']':
                    return i
                i += 1
        ans = None
        if s[0] == '[':
            ans = NestedInteger()
            _ = parse_list(s, 1, ans)
            return ans
        # just an integer
        return NestedInteger(int(s))