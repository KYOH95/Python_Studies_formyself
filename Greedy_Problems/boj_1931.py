#회의실 배정
#input: 11              output:4
#       1 4
#       3 5
#       ...

import sys
si = sys.stdin.readline

N = int(si())
a = []
for _ in range(N):
    a.append(list(map(int,si().split())))

a.sort(key = lambda x :[x[1],x[0]])

s = a[0][1]
count = 1

for i in range(1,N):
    if a[i][0] >= s:
        count += 1
        s = a[i][1]
        # print(a[i][0],a[i][1])

print(count)



"______________________________________________________________________________________________"
# # a = sorted([list(map(int,si().split())) for _ in range(N)])
# a = sorted([[1,4],[3, 5],[0, 6],[5, 7],[3, 8],[5, 9],[6, 10],[8, 11],[8, 12],[2, 13],[12, 14]],key = lambda x:x[0])

# starting = 0
# nextStart = 1000000000000000

# for i in range(0,N):
#     if a[i][1] < nextStart:
#         nextStart = a[i][1]
#         starting = i + 1
        

# count = 1
# boolcheck = True
# save = 0
# while boolcheck:
#     for i in range(starting,N):
#         currentEnd = 10000000000000
#         if a[i][0] > nextStart and a[i][1] < currentEnd:
#             currentEnd = a[i][1]
#             save = i
#             # print(a[i][0],a[i][1])
#         nextStart = a[save][1]
#         if starting == save: 
#             boolcheck = False
#             break
#         starting = save + 1
#         count += 1

# print(count)
        

