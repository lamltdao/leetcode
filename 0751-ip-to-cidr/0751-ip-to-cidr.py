class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_2_num(ip):
            arr = [int(s) for s in ip.split('.')]
            return (arr[0] << 24) + (arr[1] << 16) + (arr[2] << 8) + arr[3]
        def num_2_ip(num):
            arr = [
                (num >> 24) & 255, # first 8 bits from left to right
                (num >> 16) & 255, # next 8 bits
                (num >> 8) & 255, # next 8 bits
                num & 255 # last 8 bits
            ]
            return '.'.join([str(n) for n in arr])
        ans = []
        def process(num):
            if num == 0:
                return 32
            num_last_zeros = 0
            while not (num & 1):
                num_last_zeros += 1
                num = num >> 1
            return num_last_zeros
        while n > 0:
            num = ip_2_num(ip)
            num_last_zeros = process(num)
            for nlz in range(num_last_zeros, -1, -1):
                cover_range = 2**nlz
                if cover_range > n:
                    continue
                ans.append(num_2_ip(num) + f'/{32-nlz}')
                ip = num_2_ip(num+cover_range)
                n -= cover_range
                break
        return ans