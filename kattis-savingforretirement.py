import math
B, By, Bs, A, As = map(int, input().split(" "))
Bm = (By - B) * Bs
Ay = A + (math.ceil((Bm+1)/As))
print(int(Ay))
