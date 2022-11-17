N, X = map(int, input().split())
Ps = list(map(int, input().split()))

if __name__ == '__main__':
    for i, p in enumerate(Ps):
        if p == X:
            print(i+1)
