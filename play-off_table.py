n = int(input())
results = [input().strip().split(';') for i in range(n)]
stat = {}
wins, loses, draw, points, plays = 0, 0, 0, 0, 0
for i in range(len(results)):
    for j in range(len(results[i]) - 1):
        stat[results[i][0]] = []
        stat[results[i][2]] = []
for i in stat.keys():
    for j in results:
        plays += j.count(i)
        if (i == j[0] and int(j[1]) < int(j[3])) or (i == j[2] and int(j[1]) > int(j[3])):
            loses += 1
        elif (i == j[0] and int(j[1]) > int(j[3])) or (i == j[2] and int(j[1]) < int(j[3])):
            wins += 1
        elif (i in j and int(j[1]) == int(j[3])):
            draw += 1
    points = wins * 3 + draw
    stat[i].extend([plays, wins, draw, loses, points])
    wins, loses, draw, points, plays = 0, 0, 0, 0, 0
for i in stat.keys():
    print(i, ':', sep='', end='')
    print(*stat[i], sep=' ')
