K = int(input())
N = int(input())
time_passed = 0
data = []
for i in range(N):
    wkt, jwb = input().split(" ")
    data.append([wkt, jwb])
for dat in data:
    wkt, jwb = dat[0], dat[1]
    time_passed += int(wkt)
    if time_passed >= 210:
        hit = K
        break
    if jwb == "T" and K != 8:
        K += 1
    elif jwb == "T" and K == 8:
        K = 1
print(hit)
