N, M = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()

atotal = sum(a)

# 0 0 | 2 3 3 3 | 5 5 6
# 0  1 | 3 | 5 6 7

start = 0 # 2
for i in range(1, len(a)):
    if a[i] - a[i-1] > 1:
        start = i

tmp_discard = 0
max_discard = 0
for i in range(len(a)):
    now = (start + i)%N  # (2 + i)%9 -> 2 3 4 5 6 7 8 0 1
    if (a[now] - a[now-1])%M > 1:  # (X+1) == Mのとき、(X+1)%M == 0になるので次に進める
        max_discard = max(max_discard, tmp_discard)
        tmp_discard = 0
    tmp_discard += a[now]
max_discard = max(max_discard, tmp_discard)
print(atotal - max_discard)
