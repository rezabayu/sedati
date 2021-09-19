masukan = input()
n, h, v = masukan.split(" ")
n, h, v = int(n), int(h), int(v)

if h < (n/2):
    sa = n-h
else:
    sa = h

if v < (n/2):
    sb = n-v
else:
    sb = v

print(sa * sb)
