mat = []
for i in range(3):
    k, l, m = input().split(" ")
    mat.append([int(k), int(l), int(m)])

def find_in(listnya, elemen):
    for data in listnya:
        if elemen in data:
            a = listnya.index(data)
            b = data.index(elemen)
            return a, b

s = 0
for i in range(2, 10):
    a, b = find_in(mat, i)
    c, d = find_in(mat, i-1)
    e = ((a-c)**2 + (b-d)**2)**0.5
    s += e

print(s)
