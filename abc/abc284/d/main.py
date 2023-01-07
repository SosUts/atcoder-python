T = int(input())
import math

def make_divisors(n):
    # lower_divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i > 1:
                break
                # return i
                # lower_divisors.append(i)
            # if len(result) <= 2:
            #     result.append(i)
            # elif len(result) > 3:
            #     if result[1]**2 == result[2]:
            #         continue
            #     else:
            #         if len(result) == 4:
            #         if len(result) == 4:
            #             return result[1], result[3] # p, q
            #     # for j in range(len(lower_divisors)):
            #     #     if not result:
            #     #         result.append(lower_divisors[j])
            #     #     else:
            #     #         if lower_divisors[j]**2 != lower_divisors[j+1]
        i += 1
    return i
    # return lower_divisors

for _ in range(T):
    test_case = int(input())
    # for i in range(2, test_case+1):

    a = make_divisors(test_case)
    if (test_case%(a**2))==0:
        print(a, int(test_case/a**2))
    else:
        import math
        print(int(math.sqrt(test_case/a)), a)
    # print(test_case, l)
    # if l[1]**2 == l[2]:
    #     print(l[1], l[3])
    # elif l[1]**2 == l[3]:
    #     print(l[1], l[2])
    # elif l[2]**2 == l[3]:
    #     print(l[2], l[1])


#     p, q = 0, 0
#     for i in math.sqrt(test_case):
#         l, u = make_divisors(i)
#         if l**2*q == i:
#             print(p, q)
#         else:
#             print(q, p)
