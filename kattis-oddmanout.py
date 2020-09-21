N = int(input())
final = []
for i in range(N):
    G = int(input())
    data = input().split(" ")
    dataint = [int(x) for x in data]
    datuniq = list(set(dataint))
    for j in datuniq:
        if dataint.count(j) == 1:
            x = j
    final.append(x)

for k in range(1, len(final)+1):
    print("Case #%s: %s" % (k, final[k-1]))
