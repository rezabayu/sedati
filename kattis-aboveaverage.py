N = int(input())
final = []
for i in range(N):
    dat = input().split(" ")
    data = [int(x) for x in dat]
    jml = 0
    for j in range(1, len(data)):
        jml += data[j]
    ave = jml / data[0]
    above = 0
    for j in range(1, len(data)):
        if data[j] > ave:
            above += 1
    persen = (above/data[0])
    final.append(persen)
for k in final:
    print("{:.3%}".format(k))
