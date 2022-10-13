class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for w in words:
            for i in range(len(text) - len(w)+1):
                match = True
                for j in range(len(w)):
                    if text[i+j] != w[j]:
                        match = False
                if match:
                    ans.append([i, i+len(w)-1])
        ans.sort()
        return ans