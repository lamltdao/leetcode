class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        d = {}
        for i in range(len(secret)):
            c = secret[i]
            n = int(c)
            if n not in d:
                d[n] = OrderedDict()
            d[n][i] = None
        wrong_pos = []
        for i in range(len(guess)):
            c = guess[i]
            n = int(c)
            if n in d:
                if i in d[n]:
                    bulls += 1
                    d[n].move_to_end(i)
                    d[n].popitem()
                else:
                    wrong_pos.append(i)
        for i in wrong_pos:
            c = guess[i]
            n = int(c)
            if n in d and i not in d[n] and len(d[n]) > 0:
                cows += 1
                d[n].popitem(False)
        return str(bulls) + "A" + str(cows) + "B"
