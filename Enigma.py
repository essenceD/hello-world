enigma = {}
key, value, to_code, to_encode = [i for i in input()], [i for i in input()], [i for i in input()], [i for i in input()]
for i in range(len(key)):
    enigma[key[i]] = value[i]
for i in to_code:
    print(enigma[i], end='')
print()
for i in to_encode:
    for j in enigma.keys():
        if enigma[j] == i:
            print(j, end='')

