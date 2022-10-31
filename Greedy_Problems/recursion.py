
# 1
"""
★
★★
★★★
★★★★
★★★★★
★★★★★★
★★★★★★★
"""
def star_print(n):
    if n==0: return
    star_print(n-1)
    print('*'*n)

star_print(7) 

# 2

"""
구구단 2단
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
"""
# 재귀
def multi_table_2(n):
    if n == 0: return
    multi_table_2(n-1)
    print(f'2 * {n} = {2*n}')

multi_table_2(9)


#3
"""
5 4 3 2 1 발사
"""

# 재귀
def countdown(n):
    if n==0:
        return print("발사")
    print(n,end=" ")
    countdown(n-1)
countdown(5)

#4
"""
n~100 사이의 짝수를 구하고 싶습니다.
정수 n이 매개변수로 주어질 때, n~100 사이의 짝수를 반환하도록 함수를 완성해주세요.

제한사항
1<= n <= 100
"""
# 출력 예시 반복문
# 86 88 90 92 94 96 98 100

# 재귀

def even_num(n):
    if n>100: return
    if n%2==0:
        print(n,end=" ")
    even_num(n+1)
even_num(85)