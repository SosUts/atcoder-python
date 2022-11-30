N = int(input())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]


if __name__ == "__main__":
    d = {}
    for i, a in enumerate(A):
        if not a in d.keys():
            d[a] = []
        d[a].append(B[i])
    ans = 1
    if min(d.keys()) != 1:
        print(ans)
        import sys
        sys.exit()
    for i, k in enumerate(d.keys()):
        if k in list(d.keys())[:i+1]:
            ans = max(ans, max(d[k]))
        else:
            continue
    print(ans)
