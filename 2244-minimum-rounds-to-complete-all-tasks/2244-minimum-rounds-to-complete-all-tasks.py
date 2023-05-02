class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        for t in tasks:
            if t not in d:
                d[t] = 0
            d[t] += 1
        def get_min_round(num):
            if num == 1:
                return -1
            if num % 3 == 1:
                return 2 + (num-4) // 3
            return num // 3 + (num - 3 * (num//3) ) // 2
        ans = 0
        for num_task in d.values():
            min_round = get_min_round(num_task)
            if min_round == -1:
                return -1
            ans += min_round
        return ans
            
        