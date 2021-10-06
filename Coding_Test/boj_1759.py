#boj 1759
#10/5/21 

#암호만들기
#input:4 6                  
#      a t c i s w

L,C = map(int,input().split())

letters = list(input().split())
selected = [0 for _ in range(L)]

def is_vowel(x):
    return x in "aeiou"

def rec_func(k):
    
    if k == L:
        vowel = 0
        nvowel = 0
        for i in range(L):
            if is_vowel(letters[selected[i]]):
                vowel += 1
            else: nvowel += 1

        if vowel >=1 and nvowel>=2:
            for x in selected:
                print(letters[x],end="")
            print()

    else:
        if k==0: start=0
        else: start = selected[k-1] + 1
        for cand in range(start,C):        
            selected[k] = cand
            rec_func(k+1)
            selected[k] = 0
            


letters.sort()
rec_func(0)
