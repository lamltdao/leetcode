b cannot precede a
​
every idx, calculate using prefix sum method:
num b before it (from left)
num a after it (from right)
=> ans = min(min(num_b[i] + num_a[i])) for i in range(len(s))
​