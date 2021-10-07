#N Queen

N = int(input())
selected = [0 for _ in range(N)]
count = 0


def val_check(r1,c1,r2,c2):
    if c1==c2: return True
    if r1+c1 == r2+c2: return True
    if r1-c1 == r2-c2: return True
    return False

def rec_func(k):
    if k == N:
        global count
        count += 1
        for x in selected:
            print(x,end=' ')
        print()
    else:
        for cand in range(N):
            possible = True
            for i in range(k):
                if val_check(k,cand,i,selected[i]):
                    possible = False
                    break

            if possible:
                selected[k] = cand
                rec_func(k+1)
                selected[k] = 0


rec_func(0)
print(count)