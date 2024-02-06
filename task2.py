a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

s = set(a)
count = 0
for x in b:
    if x in s:
        count += 1

print(count)
