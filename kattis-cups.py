lines = int(input())
warna = []
jari = []
for i in range(lines):
    x, y = input().split(" ")
    if x.isalpha():
        color = x
        radius = int(y)
    else:
        color = y
        radius = int(x) / 2
    warna.append(color)
    jari.append(radius)
kamus = dict(zip(jari, warna))
jari_st = jari.copy()
jari_st.sort()
for rd in jari_st:
    print(kamus[rd])
