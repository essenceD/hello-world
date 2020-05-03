klass = {x: [] for x in range(1, 12)}
with open('c:\inputs\dataset_3380_5.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        klass[int(line[0])].append(int(line[2]))
for i, j in klass.items():
    if klass[i] == []:
        klass[i] = '-'
        continue
    klass[i] = sum(klass[i]) / len(klass[i])
for i, j in klass.items():
    print(i, j)
with open('c:\outputs\klass.txt','w') as file:
    for i, j in klass.items():
        file.write('{} {}\n'.format(i, j))
