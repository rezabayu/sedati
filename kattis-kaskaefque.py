N = int(input())
daft = []
for i in range(N):
    daft.append(int(input()))
status = 0
for j in range(N-1):
    if daft[j] - daft[j+1] > 0:
        status += 1

print(status+1)
