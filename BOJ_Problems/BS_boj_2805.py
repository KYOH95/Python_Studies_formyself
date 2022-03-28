"""
나무 자르기
link: https://www.acmicpc.net/problem/2805
"""

import sys
si = sys.stdin.readline
N,M = list(map(int,si().split()))
tree = list(map(int,si().split()))

#일정 길이를 두고 잘랐을때 남아서 가져갈 수 있는 나무들의 길이 합 구하는 메소드
def cal(tree,cut):
    sum = 0
    for x in tree:
        if x > cut:
            sum += x - cut
    return sum

#이분탐색을 활용해 조건을 만족하는 길이중 가장 작은 높이를 구하는 메소드
def bs(tree,L,R):
    ans = R+1
    while L <= R:
        mid = (L+R)//2
        if cal(tree,mid) >= M:
            L = mid+1
            ans = mid
        else:
            R = mid-1
    return ans

print(bs(tree,0,max(tree)))

