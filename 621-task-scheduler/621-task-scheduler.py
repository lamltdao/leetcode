class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_counter = {}
        for t in tasks:
            if t not in task_counter:
                task_counter[t] = 0
            task_counter[t] += 1
        max_h = []
        heapify(max_h)
        idle_time = {}
        for t in task_counter.keys():
            idle_time[t] = 0
        for t in task_counter.keys():
            heappush(max_h, (-task_counter[t], t))
        ans = 0
        wait_q = {}
        while len(max_h) > 0 or len(wait_q) > 0:
            if len(max_h) > 0:
                num_t, t = heappop(max_h)
                num_t = -num_t
                num_t -= 1
                ans+=1
                for task in idle_time.keys():
                    if idle_time[task] > 0:
                        idle_time[task] -= 1
                        if idle_time[task] == 0:
                            heappush(max_h, (-wait_q[task], task))
                            del wait_q[task]
                if num_t > 0:
                    wait_q[t] = num_t
                    idle_time[t] = n
            else: # idle
                ans += 1
                for t in idle_time.keys():
                    if idle_time[t] > 0:
                        idle_time[t] -= 1
                        if idle_time[t] == 0:
                            heappush(max_h, (-wait_q[t], t))
                            del wait_q[t]
        return ans
        