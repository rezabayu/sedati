S = int(input())
T = []
V = []
for i in range(S):
    data = input().split(" ")
    t, v = int(data[0]), float(data[1])
    T.append(t)
    V.append(v)
totals = 0
for d in range(1, S):
    vi = V[d] + V[d-1]
    ti = T[d] - T[d-1]
    totals += (vi/2) * ti/1000
print(totals)
