class Node:
    def __init__(self, name):
        self.children = {}
        self.name = name
        self.content = None
class FileSystem:

    def __init__(self):
        self.fs = Node("")

    def ls(self, path: str) -> List[str]:
        tmp = self.fs
        path = path.split("/")
        for i in range(1, len(path)):
            if path[i] == "":
                break
            tmp = tmp.children[path[i]]
        if tmp.content is None:
            return sorted([child for child in tmp.children.keys()])
        elif tmp.name != "":
            return [tmp.name]
        else:
            return []
    def mkdir(self, path: str) -> None:
        tmp = self.fs
        path = path.split("/")
        for i in range(1, len(path)):
            if path[i] not in tmp.children:
                tmp.children[path[i]] = Node(path[i])
            tmp = tmp.children[path[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        tmp = self.fs
        filePath = filePath.split("/")
        for i in range(1, len(filePath)):
            if filePath[i] not in tmp.children:
                tmp.children[filePath[i]] = Node(filePath[i])
            tmp = tmp.children[filePath[i]]
        if tmp.content is None:
            tmp.content = content
        else:
            tmp.content += content
    def readContentFromFile(self, filePath: str) -> str:
        tmp = self.fs
        filePath = filePath.split("/")
        for i in range(1, len(filePath)):
            if filePath[i] not in tmp.children:
                tmp.children = Node(filePath[i])
            tmp = tmp.children[filePath[i]]
        return tmp.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)