Create two hash tables:
- valid_directions: {street_num: [directions that can be gone from that street num]}
- valid_connections: {direction: [street nums that can be connected in that direction]}
Create function dfs(r,c):
```
def dfs(r,c):
> Update visited
> Get street_num
> Init valid_path = False
> Check each cell in 4 dirs:
>> if dir in valid_directions[street_num] and (cell not out of range) and cell not visited and cell in valid_connections[dir] then:
>>> valid_path = dfs(cell) OR valid_path
> return valid_path
```
return dfs(0,0)