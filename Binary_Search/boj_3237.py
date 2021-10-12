#두수의 합

import sys
si = sys.stdin.readline

N = int(si())
Nlist = list(map(int,si().split()))
X = int(si())

Nlist.sort()
# used = []
def BS(a,x,L,R):
    # if i in used: return False
    while(L<=R):
        M = (L+R)//2
        if a[M] == x:
            # used.append(i)
            # used.append(x)
            return True
        elif a[M] < x: L = M+1 
        else: R = M-1
    return False


count = 0
for i in range(N-1):
    if BS(Nlist,X-Nlist[i],i+1,N-1): count += 1

# print(used)
print(count)


















# import sys
# si = sys.stdin.readline

# N = int(si())
# N_list = list(map(int,si().split()))
# X = int(si())

# N_list.sort()

# used = []
# def binary_search(list,i,X,L,R):
#     if i in used: return False
#     while L <= R:
#         M = (L+R)//2
#         if list[M] + i == X:
#             used.append(i)
#             used.append(list[M])
#             return True
#         if list[M] + i < X: L = M + 1
#         if list[M] + i > X: R = M - 1
#     return False

# count = 0
# for i in N_list:
#     if binary_search(N_list,i,X,0,N-1):
#         print(i)
#         count+=1

# print(count)