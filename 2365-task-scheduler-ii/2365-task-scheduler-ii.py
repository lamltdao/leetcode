class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_task_time = {}
        cur_time = 1 # time before executing task t
        for t in tasks:
            if t in next_task_time:
                cur_time = max(cur_time, next_task_time[t])
            next_task_time[t] = cur_time + space + 1
            cur_time += 1
        return cur_time-1
    