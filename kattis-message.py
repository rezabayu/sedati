n = int(input())
final = []
for i in range(n):
    text = input()
    a = len(text)
    b = a
    while not (b**0.5).is_integer():
        b += 1
    c = b-a
    d = int(b**0.5)
    text = text + ("*"*c)
    text_mt = []
    for j in range(0, b, d):
        text_mt.append(text[j:(j+d)])
    text_tp = []
    for k in range(0, d):
        for l in range(d-1, -1, -1):
            text_tp.append(text_mt[l][k])
    akhir = "".join(text_tp)
    akhire = akhir.replace("*","")
    final.append(akhire)
for m in final:
    print(m)
