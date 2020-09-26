N = int(input())
tmax = list(map(int, input().split(" ")))
tmax_src = []
for i in range(N-2):
    t = max([tmax[i], tmax[i+2]])
    tmax_src.append(t)
tru = min(tmax_src)
print(tmax_src.index(tru)+1, tru)
