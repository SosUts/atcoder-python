from collections import defaultdict, deque
import sys

N = int(input())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]


if __name__ == "__main__":
    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(B[i])
        d[B[i]].append(a)
    q = deque()
    q.append(1)
    reached = {1}

    while q:
        f = q.popleft()
        for i in d[f]:
            if not i in reached:
                q.append(i)
                reached.add(i)

    print(max(reached))
