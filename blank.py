#practice
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
B = [(x, i) for i, x in enumerate(a)]
B.sort()

print(a)
print(B)