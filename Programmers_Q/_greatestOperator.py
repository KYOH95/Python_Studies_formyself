"""
[카카오 인턴쉽] 수식 최대화
link: https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
"""

def calculator_1op(queue_n,queue_op,op1):
    num_list = [queue_n[0]]
    op_list = []
    for i in range(len(queue_op)):
        if queue_op[i] == op1:
            if op1 == '+': num_list[-1] += queue_n[i+1]
            elif op1 == '-': num_list[-1] -= queue_n[i+1]
            elif op1 == '*': num_list[-1] *= queue_n[i+1]
        else:
            num_list.append(queue_n[i+1])
            op_list.append(queue_op[i])
    return num_list,op_list

def calculator_2op(Q_num,Q_op,op1,op2):
    num_list,op_list = calculator_1op(Q_num,Q_op,op1)
    result1,result2 = calculator_1op(num_list,op_list,op2)
    return abs(result1[0])

def calculator_3op(Q_num,Q_op,op1,op2,op3):
    num_list,op_list = calculator_1op(Q_num,Q_op,op1)
    num_list,op_list = calculator_1op(num_list,op_list,op2)
    result1,result2 = calculator_1op(num_list,op_list,op3)
    return abs(result1[0])

def solution(expression):
    answer = []
    operator = set()
    Q_num = []
    Q_op = []
    temp = ''
    for x in expression:
        if x == '-' or x == '+' or x == '*':
            operator.add(x)
            Q_num.append(int(temp))
            Q_op.append(x)
            temp = ''
        else:
            temp += x
    Q_num.append(int(temp))
    if len(operator) == 1:
        for i in operator:
            a,b = calculator_1op(Q_num,Q_op,i)
            answer.append(int(abs(a[0])))
    elif len(operator) == 2:
        for i in operator:
            for j in operator:
                if i == j: continue
                answer.append(calculator_2op(Q_num,Q_op,i,j))
    else:
        for i in operator:
            for j in operator:
                for k in operator:
                    if i == j or j==k or i==k: continue
                    answer.append(calculator_3op(Q_num,Q_op,i,j,k))

    return max(answer)

print(solution("100-200*300-500+20"))
# solution("100+200+300+500+20")
