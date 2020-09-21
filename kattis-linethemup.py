names = []
N = int(input())
for i in range(N):
    names.append(input())
y = names.copy()
y.sort()
z = names.copy()
z.sort(reverse=True)
if names == y:
    print('INCREASING')
elif names == z:
    print('DECREASING')
else:
    print('NEITHER')
