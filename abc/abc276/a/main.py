s = input()
x = -100
for i in range(len(s)):
    if s[i] == "a":
        x = i+1

print(x if x != -100 else -1)
