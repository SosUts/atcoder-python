import re
S = input()
pattern = r"^([A-Z]){1}[1-9]\d{5}([A-Z]){1}$"
# print(re.search(pattern, "Q142857Z"))
print("Yes" if re.search(pattern,S) else "No")
