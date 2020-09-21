final = []
while True:
    N = input()
    if N == '0':
        break
    sumo = 0
    for i in N:
        sumo += int(i)
    for j in range(100, 10, -1):
        k = str(int(N) * j)
        sumi = 0
        for la in k:
            sumi += int(la)
        if sumi == sumo:
            this = int(j)
    final.append(this)
for m in final:
    print(m)
