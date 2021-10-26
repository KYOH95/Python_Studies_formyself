#boj_11728
#배열 합치기  

#수정 필요!
# import sys
# si = sys.stdin.readline

# N,M = map(int,si().split())
# a = list(map(int,si().split()))
# b = list(map(int,si().split()))
# c = []

# R = 0
# if N >= M:
#     for L in range(N):
#         while R + 1 < M and b[R] <a[L]:
#             c.append(b[R])
#             R += 1
#         c.append(a[L])

# else:
#     for L in range(M):
#         while R + 1 < N and a[R] <b[L]:
#             c.append(a[R])
#             R += 1
#         c.append(b[L])

# for x in c:
#     print(x,end=" ")
