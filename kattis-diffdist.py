final = []
while True:
    data = input()
    if data == "0":
        break
    x1, y1, x2, y2, p = map(float, data.split(" "))
    dist = ((abs(x1-x2))**p + (abs(y1-y2))**p)**(1/p)
    final.append(dist)
for ghu in final:
    print(ghu)
