class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.mapping = {} # {name: {num_col, rows: {row_id: values}, auto_id: 1}}
        n = len(names)
        for i in range(n):
            self.mapping[names[i]] = {
                'num_col': columns[i],
                'rows': {}, # {row_id: values}
                'auto_id': 1
            }
    def insertRow(self, name: str, row: List[str]) -> None:
        new_row_id = self.mapping[name]['auto_id']
        self.mapping[name]['auto_id'] += 1
        self.mapping[name]['rows'][new_row_id] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.mapping[name]['rows'][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.mapping[name]['rows'][rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)