import math
N = int(input())

def tinggi(v0, t, ang):
    tinggi = v0 * t * math.sin(ang) - 0.5 * 9.81 * (t**2)
    return tinggi

def waktu(x1, v0, ang):
    waktu = x1 / (v0 * math.cos(ang))
    return waktu

hasil = []
for i in range(N):
    data = input().split(" ")
    v0, ang, x1, h1, h2 = float(data[0]), float(data[1]) * math.pi / 180 , float(data[2]), float(data[3]), float(data[4])
    t = waktu(x1, v0, ang)
    h_place = tinggi(v0, t, ang)
    if (h2 - h_place >= 1) and (h_place - h1 >= 1):
        safety = 'Safe'
    else:
        safety = 'Not Safe'
    hasil.append(safety)

for res in hasil:
    print(res)
