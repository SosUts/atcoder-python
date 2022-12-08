N, M = map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
a, b = [list(i) for i in zip(*ab)]

from collections import defaultdict
from operator import itemgetter, attrgetter
D = defaultdict(list)

for m in range(M):
    D[a[m]].append(b[m])
    D[b[m]].append(a[m])
for n in range(1,N+1):
    if D[n]:
        print(len(D[n]), *sorted(D[n]))
    else:
        print(0)
