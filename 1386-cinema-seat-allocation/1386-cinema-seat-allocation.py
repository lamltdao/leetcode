class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        type 0: 1, 10 reserved
        
        type 1: s2,s3 reserved => sit from 4
        type 2: 4,5 => sit at 6789
        type 3: 6,7 => sit at 5432
        typ3 4: 8,9: sit from 7 to left
        
        type 1 or 4: <= 1
        
        
        2 if 1 or 10 or none is reserved
        0 if 1 + 3 + .. or 2 + 4 + .. or 2 + 3
        1 otherwise
        
        sort reservedSeats by row numbers
        """
        num_cant_seat = 0
        reserved_types = {}
        def check(row):
            row_reserved_type = reserved_types[row]
            nonlocal num_cant_seat
            if (1 in row_reserved_type and 3 in row_reserved_type) or (2 in row_reserved_type and 4 in row_reserved_type) or (2 in row_reserved_type and 3 in row_reserved_type):
                    num_cant_seat += 2
            elif len(row_reserved_type) == 0 or (0 in row_reserved_type and len(row_reserved_type) == 1):
                num_cant_seat += 0
            else:
                num_cant_seat += 1
        for i in range(len(reservedSeats)):
            rseat = reservedSeats[i]
            row, num = rseat[0], rseat[1]
            if row not in reserved_types:
                reserved_types[row] = set()
            if num == 1 or num == 10:
                reserved_types[row].add(0)
            elif num == 2 or num == 3:
                reserved_types[row].add(1)
            elif num == 4 or num == 5:
                reserved_types[row].add(2)
            elif num == 6 or num == 7:
                reserved_types[row].add(3)
            elif num == 8 or num == 9:
                reserved_types[row].add(4)
        for row in reserved_types.keys():
            check(row)
        return 2*n - num_cant_seat
                