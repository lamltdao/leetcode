class Node:
    def __init__(self):
        self.children = {}
        self.value = 0
    def insert(self, list_path, value):
        tmp = self
        for i in range(1,len(list_path)):
            d = list_path[i]
            if d not in tmp.children:
                if i != len(list_path)-1: # parent path does not exist
                    return False
                tmp.children[d] = Node()
            tmp = tmp.children[d]
        if tmp.value > 0: # already exist
            return False
        tmp.value = value
        return True
    def get_val(self, list_path):
        tmp = self
        for i in range(1,len(list_path)):
            d = list_path[i]
            if d not in tmp.children:
                return -1 # path does not exist
            tmp = tmp.children[d]
        # if tmp.value > 0:
        return tmp.value
        # return -1
class FileSystem:

    def __init__(self):
        self.trie = Node()

    def createPath(self, path: str, value: int) -> bool:
        list_path = path.split("/")
        return self.trie.insert(list_path, value)

    def get(self, path: str) -> int:
        list_path = path.split("/")
        return self.trie.get_val(list_path)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)