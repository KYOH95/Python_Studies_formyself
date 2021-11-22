#잃어버린 괄호
#input = 55-50+40       output: -35
import sys
si = sys.stdin.readline

s = si()
temp = ''
ans = 0
last_op = True #if Ture, possitive

for i in range(0,len(s)):
    # When operator
    if s[i] == '+' or s[i] == '-':
        if last_op == True:
            ans += int(temp)
        else:
            ans -= int(temp)
        temp = ''
        if s[i] == '-': last_op = False
        # print(f'ans = ',ans)

    #when number
    else: 
        temp += s[i]

    #for the last numbers
    if i == len(s)-1:
        if last_op == True:
            ans += int(temp)
        else:
            ans -= int(temp)

print(ans)

