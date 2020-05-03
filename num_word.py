tabel = {}
average, sMath, sPhys, sRus, num, ans = 0, 0, 0, 0, 0, ''

def listsum(a):
    s = 0
    for i in a:
        s += int(i)
    return s

with open('c:\inputs\dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        key, *value = line.strip().split(';')
        tabel[key] = value
for i, j in tabel.items():
    average = listsum(tabel[i]) / len(tabel[i])
    ans += str(average) + '\n'
print(ans)
for i in tabel.values():
    sMath += int(i[0])
    sPhys += int(i[1])
    sRus += int(i[2])
    num += 1
ans += str(sMath / num) + ' ' + str(sPhys / num) + ' ' + str(sRus / num)
with open('c:\outputs\journal.txt', 'w') as ouf:
    ouf.write(ans)