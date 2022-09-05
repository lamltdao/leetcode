class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        monostack
        [76,75,74,73]
        """
        mono_stack = []
        mono_stack.append((temperatures[-1], len(temperatures)-1))
        ans = [0 for _ in temperatures]
        for i in range(len(temperatures)-2,-1,-1):
            while len(mono_stack) > 0 and temperatures[i] >= mono_stack[-1][0]:
                mono_stack.pop()
            if len(mono_stack) > 0:
                ans[i] = mono_stack[-1][1] - i
            mono_stack.append((temperatures[i], i))
        return ans