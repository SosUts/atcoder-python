import sys
import math
math.gcd(2, 4)
N = int(input())
A = [x for x in map(int, input().split())]

if len(set(A)) == 1:
    print(0)
    sys.exit()
ans = 0
g = 0
for a in A:
    g = math.gcd(a, g)
l = []

"""
gcd(A)でやめないと最小回数にならない
(例)
3
15 30 45なら15でやめないといけない
"""
for a in A:
    a /= g
    while a%2 == 0:
        a //= 2
        ans += 1
    while a%3 == 0:
        a //= 3
        ans += 1
    l.append(a)
print(ans if len(set(l)) == 1 else -1)
