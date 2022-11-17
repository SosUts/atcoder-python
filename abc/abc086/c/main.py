import sys

N = int(input())
txy = [map(int, input().split()) for _ in range(N)]
t, x, y = [list(i) for i in zip(*txy)]

if __name__ == "__main__":
    for i in range(N):
        if i == 0:
            dt, dx, dy = t[0], x[0], y[0]
        else:
            dt = t[i] - t[i-1]
            dx = abs(x[i] - x[i-1])
            dy = abs(y[i] - y[i-1])
        if dt < dx + dy:
            print("No")
            sys.exit()
        elif dt%2 != (dx + dy)%2:
            print("No")
            sys.exit()
        else:
            continue
    print("Yes")
