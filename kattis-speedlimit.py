result = []
while True:
    n = int(input())
    if n == -1:
        break
    V = []
    T = []
    for i in range(n):
        data = input().split(" ")
        v, t = int(data[0]), int(data[1])
        V.append(v)
        T.append(t)
    si = 0
    for a in range(len(V)):
        if a > 0:
            ti = T[a] - T[a-1]
        else:
            ti = T[a]
        vi = V[a]
        si += (vi * ti)
    result.append(si)
for hasil in result:
    print("%s miles" % hasil)
