class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = {}
        for i,w in enumerate(wordsDict):
            if w not in d:
                d[w] = []
            d[w].append(i)
        # d[word] already sorted
        if word1 == word2:
            indices = d[word1]
            ans = len(wordsDict)
            for i in range(len(indices)-1):
                ans = min(ans, indices[i+1] - indices[i])
            return ans
        else:
            indices_1, indices_2 = d[word1], d[word2]
            """
            1,2,4,5
            3,6
            """
            ptr1 = ptr2 = 0
            ans = abs(indices_1[ptr1] - indices_2[ptr2])
            while ptr1 < len(indices_1) and ptr2 < len(indices_2):
                ans = min(ans, abs(indices_1[ptr1] - indices_2[ptr2]))
                if indices_1[ptr1] < indices_2[ptr2]:
                    ptr1 += 1
                else:
                    ptr2 += 1
            return ans