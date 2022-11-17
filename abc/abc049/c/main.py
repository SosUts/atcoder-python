if __name__ == "__main__":
s1 = input()
s1 = "dreameraser"
l = ["dream", "dreamer", "erase", "eraser"]
if len(s1) <= 4:
    print("NO")

i = 5
while True:
    print(i, s1)
    if s1[-i:] in l:
        s1 = s1[:-i]
        i = 1
        continue
    elif s1 == "":
        print("YES")
        break
    elif len(s1) <= 4 or i == 7:
        print("NO")
        break
    else:
        i += 1
