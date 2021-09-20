#잃어버린 괄호
#input = 55-50+40       output: -35
#!실패


s = input()

s_temp = s.replace('+','-')

s_number = s_temp.split('-')
s_plus_minus = []

for i in range(0,len(s)):
    if s[i] =='-':
        s_plus_minus.append(0)
    elif s[i] =='+':
        s_plus_minus.append(1)

print(s_plus_minus)
data = []


print(data)