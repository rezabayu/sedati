X = int(input())
d = [a for a in str(X)]
d.sort()
final = []
for i in range(X+1, 10**len(d)):
    e = [b for b in str(i)]
    e.sort()
    if e == d:
        final.append(i)
        break
if len(final) > 0:
    print(i)
else:
    print(0)
