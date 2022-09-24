class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = []
        def flatten(flatten_arr, arr_in):
            for el in arr_in:
                if type(el) == int:
                    flatten_arr.append(el)
                else:
                    flatten(flatten_arr, el)
        flatten(self.vec, vec)
        self.idx = -1
    def next(self) -> int:
        self.idx += 1
        return self.vec[self.idx]
    def hasNext(self) -> bool:
        return self.idx+1 < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()