n = int(input())
data = input().split(" ")
data_in = [int(x) for x in data]
data_in.sort(reverse=True)
hari = []
for y in range(n):
    z = data_in[y] + y + 2
    hari.append(z)
hari.sort()
print(hari[-1])
