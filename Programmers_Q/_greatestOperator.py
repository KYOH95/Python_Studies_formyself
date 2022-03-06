"""
[카카오 인턴쉽] 수식 최대화
link: https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
"""

from collections import deque

def calculator_1op(queue_n,queue_op,op1):
    num_list = [queue_n[0]]
    op_list = []
    queue_n.popleft()
    for i in range(len(queue_op)):
        if queue_op[i] == op1:
            if op1 == "+": num_list[-1] += queue_n[i]
            elif op1 == '-': num_list[-1] -= queue_n[i]
            elif op1 == '*': num_list[-1] *= queue_n[i]
        else:
            num_list.append(queue_n[i])
            op_list.append(queue_op[i])
    return num_list,op_list

def calculator_2op(Q_num,Q_op,op1,op2):
    num_list,op_list = calculator_1op(Q_num,Q_op,op1)
    num_list = deque(num_list)
    result1,result2 = calculator_1op(num_list,op_list,op2)
    return result1

def calculator_3op(Q_num,Q_op,op1,op2,op3):
    num_list,op_list = calculator_1op(Q_num,Q_op,op1)
    num_list = deque(num_list)
    num_list,op_list = calculator_1op(num_list,op_list,op2)
    num_list = deque(num_list)
    result1,result2 = calculator_1op(num_list,op_list,op3)
    return result1

def solution(expression):
    answer = 0
    operator = set()
    Q_num = deque()
    Q_op = deque()
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

    a = calculator_3op(Q_num,Q_op,'*','+','-')
    print(a)

    return answer

solution("100-200*300-500+20")