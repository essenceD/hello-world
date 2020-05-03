n = int(input())
way = [input().lower().split() for i in range(n)]
location = [ 0, 0]
for i in way:
    if i[0] == 'север':
        location[1] += int(i[1])
    elif i[0] == 'юг':
        location[1] -= int(i[1])
    elif i[0] == 'восток':
        location[0] += int(i[1])
    elif i[0] == 'запад':
        location[0] -= int(i[1])
print(*location)