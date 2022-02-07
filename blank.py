

def BF(k,n,selected,info):
    
    if k == n:
        ryan_list = [0 for _ in range(0,11)]
        for x in selected:
            ryan_list[x] += 1
            
    else:
        for point in range(0,11):
            selected[k] = point
            
            if selected.count(point) <= info[point]+1:
                BF(k+1,n,selected,info)

print()
print("----------------------------------")

n = 5
selected = [0 for _ in range(n)]
print(BF(0, n, selected,[2,1,1,1,0,0,0,0,0,0,0]))