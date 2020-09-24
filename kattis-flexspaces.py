x, y = input().split(" ")
part = input().split(" ")
hasil = []
for i in range(int(y)):
    a = int(x) - int(part[i])
    hasil.append(int(part[i]))
    hasil.append(a)
hasil.append(int(x))
for i in range(int(y)-1, -1, -1):
    for j in range(int(y)-2, -1, -1):
        b = abs(int(part[i])-int(part[j]))
        hasil.append(b)
final = list(set(hasil))
if 0 in final:
    final.remove(0)
final.sort()
print(*final)
