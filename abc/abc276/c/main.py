N = int(input())
p = list([int(i) for i in input().split()])

import copy
import sys

for i in range(N-1, -1, -1):
    if p[i-1] - p[i] > 0:
        head = p[0:i]
        tail = p[i:]
        # print(head)
        # print(tail)
        break
small = [x for x in tail if x < head[-1]]
index = small.index(max(small))
head[-1], tail[index] = tail[index], head[-1]
tail.sort(reverse=True)
print(*head, *tail)
