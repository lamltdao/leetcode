class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        sig_byte_idx = 0
        while sig_byte_idx < len(data):
            # get longest 1s
            num_byte = 0
            for i in range(7,-1,-1):
                if (data[sig_byte_idx] & (1 << i)) >> i: # = 1
                    num_byte += 1
                else:
                    break
                
            if num_byte == 1 or num_byte > 4:
                return False
            if num_byte == 0:
                sig_byte_idx += 1
                continue
            # check subsequent num_byte bytes to see if they start with 10
            for i in range(1, num_byte):
                if sig_byte_idx + i < len(data):
                    if not ((data[sig_byte_idx + i] & (1 << 7)) >> 7) or ((data[sig_byte_idx + i] & (1 << 6)) >> 6):
                        return False
                else:
                    return False
            sig_byte_idx += num_byte
        return True