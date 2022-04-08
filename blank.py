from collections import deque
Q = []
q = deque([])
q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q)
q.popleft()
print(q)