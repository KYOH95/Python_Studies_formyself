#1182
#부분수열의 합
#10/5/21

N,S = map(int,input().split())
numbers = list(map(int,input().split()))
selected = [0 for _ in range(N)]

count = 0
def rec_func(k,value):
    if k == N:
        if value == S:
            global count
            count += 1
    else:
        rec_func(k+1,value + numbers[k])
        rec_func(k+1,value)





rec_func(0,0)
if S == 0: count -= 1
print(count)





# count = 0

# def rec_func(k):
#     global count
#     if k == N:
#         sum_ = 0
#         if sum(selected)==0:
#             pass
#         else:
#             for i in range(N):
#                 if selected[i] == 1:
#                     sum_ += numbers[i]
#             if sum_ == S: count += 1
#     else:
#         for cand in range(0,2):
#             selected[k] = cand
#             rec_func(k+1)
#             selected[k] = 0

# rec_func(0)
# print(count)