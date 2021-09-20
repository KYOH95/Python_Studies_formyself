#문자와 숫자 받고 문자는 오름차순으로 숫자는 더해서 출력하기
#input : K1KA5CB7               output: ABCKK13
#input : AJKDLSI412K4JSJ9D      output: ADDIJJJKKLSS20

s = input()

chr_ = []
num_ = []

sum = 0
for i in range(0,len(s)):
    if ord('A') <= ord(s[i]) <= ord('Z'):
        chr_.append(s[i])
    else:
        sum += int(s[i])

chr_.sort()


for i in chr_:
    print(i,end='')

print(sum)