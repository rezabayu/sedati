s, t, n = input().split(" ")
s, t, n = int(s), int(t), int(n)
d = input().split(" ")
b = input().split(" ")
c = input().split(" ")

boys = s
bus = 0
for i in range(n):
    boys += int(d[i])
    bus += int(c[i])
    if bus > boys:
        boys += bus - boys
    boys += int(b[i])

boys += int(d[-1])
if boys <= t:
    print("yes")
else:
    print("no")
