errors = set()
n = int(input())
slova = [input().lower() for i in range(n)]
m = int(input())
to_check = [input().lower().split() for i in range(m)]
for i in to_check:
    for j in i:
        if j not in slova:
            errors.add(j)
for i in errors:
    print(i)