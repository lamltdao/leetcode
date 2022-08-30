Create next_task_time {task type: time}, the time to execute the next task of type [task type], and cur_time, the current time before executing the next task.
```python
for each task t:
if t in next_task_time, i.e t is the next task of its type to be executed:
cur_time = max(cur_time, next_task_time[t]) # forward cur_time to the time to execute task t
next_task_time[t] = cur_time + space+1 # update the time to execute next task of same type as task t
cur_time += 1 # inc cur_time
return cur_time - 1 # problem asks for number of days all tasks are completed, while at the last iteration, after the last task is executed, we inc cur_time. Thus, we need to dec cur_time and return that value
```