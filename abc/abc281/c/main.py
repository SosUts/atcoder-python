N, T = map(int, input().split())
A = list(map(int, input().split()))

one_cycle = sum(A)

target_cycle = T%one_cycle

total = 0
for i in range(len(A)):
    if total + A[i] >= target_cycle:
        print(i+1, target_cycle-total)
        break
    total += A[i]
