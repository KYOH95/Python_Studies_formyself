#N-Queen
#10/5/21

N = int(input())
col = [0 for _ in range(N)]
count = 0

def attack_check(r1,c1,r2,c2):
    if c1 == c2: return True
    if r1 + c1 == r2 + c2: return True
    if r1 - c1 == r2 - c2: return True
    return False

def rec_fucn(k):
    if k == N:
        global count 
        count += 1

    else:
        for cand in range(N):
            possible = True
            for j in range(k):
                if attack_check(k,cand,j,col[j]):
                    possible = False
                    break
            
            if possible:
                col[k] = cand
                rec_fucn(k+1)
                col[k] = 0


rec_fucn(0)
print(count)