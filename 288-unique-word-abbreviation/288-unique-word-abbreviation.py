class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbre_dict = {}
        for w in dictionary:
            abbrev = self.getAbbrev(w)
            if abbrev not in self.abbre_dict:
                self.abbre_dict[abbrev] = set()
            self.abbre_dict[abbrev].add(w)
    def getAbbrev(self, word):
        return word if len(word) == 2 else word[0] + str(len(word)-2) + word[-1]
    def isUnique(self, word: str) -> bool:
        abbrev = self.getAbbrev(word)
        if abbrev not in self.abbre_dict or (word in self.abbre_dict[abbrev] and len(self.abbre_dict[abbrev]) == 1):
            return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)