class Solution:
    def backtrack(self, pos, word,table, digits,res):
        if pos == len(digits):
            res.append(''.join(word))
            return
        for c in table[int(digits[pos])]:
            word.append(c)
            self.backtrack(pos+1, word, table, digits,res)
            word.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        table = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r', 's'],
            8: ['t','u','v'],
            9: ['w','x','y', 'z']
        }
        
        res = []
        word = []
        self.backtrack(0, word,table, digits, res)
        return res
