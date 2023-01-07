N, M = map(int, input().split())

edges = [list(map(int, input().split())) for l in range(M)]

from collections import deque, defaultdict
d = defaultdict(list)
que = deque()

for e in edges:
    d[e[0]].append(e[1])
    d[e[1]].append(e[0])
# print(d)
visited = [-1]*(N+1)
visited[0] = 1
ans = 0
for n in range(1, N+1):
    if visited[n] != -1:
        # print("visited ", n)
        continue
    visited[n] = 1
    que.append(n)
    while que:
        v = que.popleft()
        for i in d[v]:
            if visited[i] != -1:
                continue
            visited[i] = 1
            que.append(i)
    # print(n)
    ans += 1
print(ans)
