class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        # {task_num: num occurences}
        # if each task_num can be completed in rounds of 2 or 3, i.e != 1
        for t in tasks:
            if t not in d:
                d[t] = 0
            d[t] += 1
        MAX = 10**6
        max_num_task = max(d.values())
        dp_min_round = [MAX for _ in range(max_num_task+1)]
        dp_min_round[0] = 0
        for i in range(2, max_num_task+1):
            dp_min_round[i] = min(dp_min_round[i], dp_min_round[i-2]+1)
            if i >= 3:
                dp_min_round[i] = min(dp_min_round[i], dp_min_round[i-3]+1)
        ans = 0
        for num_task in d.values():
            if num_task == 1:
                return -1
            if dp_min_round[num_task] >= MAX:
                return -1
            ans += dp_min_round[num_task]
        return ans
            
        