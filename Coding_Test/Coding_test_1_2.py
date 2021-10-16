import sys
from collections import deque
si = sys.stdin.readline

h,w,r = map(int,si().split())
a = [[]for _ in range(h)]
b = [[0] * w for _ in range(h)]
for i in range(h):
    a[i] = list(map(int,si().split()))
for i in range(h):
    for j in range(w):
        b[i][j] = a[i][j]
    
#문자!
r_atk = [[]for _ in range(r)]
r_def = [[]for _ in range(r)]
for i in range(r):
     r_atk[i]= list(si().split())
     rtemp1,rtemp2 = map(int,si().split())
     r_def[i] = [rtemp1-1,rtemp2-1]

     
def bfs_d(x,y):    
    if a[x][y] == 0:
        a[x][y] = b[x][y]

#        E      W     S     N
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y,EWSN):
    global count
    queue = deque()
    if a[x][y] == 0: return
    queue.append(x)
    queue.append(y)

    if EWSN == 'E':
        direction = 0
    elif EWSN == 'W':
        direction = 1
    elif EWSN == 'S':
        direction = 2
    elif EWSN == 'N':
        direction = 3

    while queue:
        x = queue.popleft()
        y = queue.popleft()
        height = a[x][y]
        a[x][y] = 0
        count += 1     
        for i in range(int(height)):
            dx = dir[direction][0] * i
            dy = dir[direction][1] * i
            nx = x + dx 
            ny = y + dy
            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            if a[nx][ny] == 0: continue
            queue.append(nx)
            queue.append(ny)
        
count = 0
for i in range(r):
    bfs(int(r_atk[i][0])-1,int(r_atk[i][1])-1,r_atk[i][2])
    bfs_d(r_def[i][0],r_def[i][1])

print(count)
for i in range(h):
    for j in range(w):
        if a[i][j] == 0: print('F',end=" ")
        else: print('S',end=" ")
    print()

