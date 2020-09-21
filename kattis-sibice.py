N, W, H = input().split(" ")
N, W, H = int(N), int(W), int(H)
diag = (W**2 + H**2)**0.5
res = []
for i in range(N):
    l = int(input())
    if l <= diag:
        res.append("DA")
    else:
        res.append("NE")
for hsl in res:
    print(hsl)
