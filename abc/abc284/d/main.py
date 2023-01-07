T = int(input())
import math

def first_factor(n):
    i = 1
    while True:
        if n % i == 0:
            if i > 1:
                break
        i += 1
    return i

for _ in range(T):
    test_case = int(input())
    f = first_factor(test_case)
    if test_case%f**2 == 0:
        print(f, test_case//f**2)
    else:
        print(int(math.sqrt(test_case/f)), f)
