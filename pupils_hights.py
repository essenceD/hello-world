_сlass = {x: [] for x in range(1, 12)}
with open('c:\inputs\dataset_3380_5.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        _сlass[int(line[0])].append(int(line[2]))
for i, j in _сlass.items():
    if _сlass[i] == []:
        _сlass[i] = '-'
        continue
    _сlass[i] = sum(_сlass[i]) / len(_сlass[i])
for i, j in _сlass.items():
    print(i, j)
with open('c:\outputs\сlass.txt','w') as file:
    for i, j in _сlass.items():
        file.write('{} {}\n'.format(i, j))
