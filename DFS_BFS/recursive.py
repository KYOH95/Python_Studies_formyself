# 9/20/2021

# def recursive_function(i):
#     if i == 100:
#         return
#     print(f"{i+1}번째 재귀함수를 호출합니다.")
#     recursive_function(i+1)

# recursive_function(0) 



#factorial 구하기

def factorial_function(n):
    if n <= 1:
        return 1

    return n * factorial_function(n-1)

print(factorial_function(5)) 