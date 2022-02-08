
n = 5
M = 2
selected = ['' for _ in range(M)]
# used = [0 for _ in range(0,n+1)]
order = "ABCDE"

def rec_(k):
    if k == M:
        print(selected)
    else:
        if k == 0: start = 0
        # else: start = order.index(selected[k-1])+1
        for cand in range(start,n):
            selected[k] = order[cand]
            rec_(k+1)
            
            
        
rec_(0)

# order = "ABCDE"
# print(order[4])