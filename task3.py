nums = list(map(int, input().split()))
seen = set()

for x in nums:
    if x in seen:
        print("YES") 
    else:
        print("NO")
        seen.add(x)
