class SnapshotArray:

    def __init__(self, length: int):
        """
        {snap_id: array} => 25 * 10^8
        array: [val]
        snap [[(val, snap_id)], ]
        
        snap: for each idx i
            append (array[i], snap_id)
        set: modify array
        get: look at snap, use binary search to find val
        """
        self.length = length
        self.snaps = [[(0, -1)] for _ in range(length)]
        self.cur_snap_id = -1

    def set(self, index: int, val: int) -> None:
        if len(self.snaps[index]) > 0 and self.snaps[index][-1][1] != self.cur_snap_id+1:
            self.snaps[index].append((val, self.cur_snap_id+1))
        else:
            self.snaps[index][-1] = (val, self.cur_snap_id+1)
    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id
    def get(self, index: int, snap_id: int) -> int:
        # loop through self.snaps[index] to find latest change <= snap_id
        arr = self.snaps[index]
        l = 0
        r = len(arr)-1
        valid = None
        while l <= r:
            m = (l+r) // 2
            if arr[m][1] == snap_id:
                return arr[m][0]
            elif arr[m][1] < snap_id:
                valid = m
                l = m+1
            else:
                r = m-1
        return arr[valid][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)