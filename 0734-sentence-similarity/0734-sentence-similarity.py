class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        n = len(sentence1)
        similarPairs = set([tuple(p) for p in similarPairs])
        for i in range(n):
            if sentence1[i] == sentence2[i] or (sentence1[i], sentence2[i]) in similarPairs or (sentence2[i], sentence1[i]) in similarPairs:
                continue
            else:
                return False
        return True