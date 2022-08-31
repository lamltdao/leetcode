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
        reservedSeats.sort(key = lambda s: s[0])
        tmp_row = reservedSeats[0][0]
        tmp_row_reserved_types = set()
        num_cant_seat = 0
        def check():
            nonlocal num_cant_seat
            if (1 in tmp_row_reserved_types and 3 in tmp_row_reserved_types) or (2 in tmp_row_reserved_types and 4 in tmp_row_reserved_types) or (2 in tmp_row_reserved_types and 3 in tmp_row_reserved_types):
                    num_cant_seat += 2
            elif len(tmp_row_reserved_types) == 0 or (0 in tmp_row_reserved_types and len(tmp_row_reserved_types) == 1):
                num_cant_seat += 0
            else:
                num_cant_seat += 1
        for rseat in reservedSeats:
            row, num = rseat[0], rseat[1]
            if row != tmp_row:
                # about to change row. Check prev row how many seat it has
                check()
                tmp_row = row
                tmp_row_reserved_types = set()
            if num == 1 or num == 10:
                tmp_row_reserved_types.add(0)
            elif num == 2 or num == 3:
                tmp_row_reserved_types.add(1)
            elif num == 4 or num == 5:
                tmp_row_reserved_types.add(2)
            elif num == 6 or num == 7:
                tmp_row_reserved_types.add(3)
            elif num == 8 or num == 9:
                tmp_row_reserved_types.add(4)
        check()
        return 2*n - num_cant_seat
                