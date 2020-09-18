X = int(input())
N = int(input())
left = 0
for i in range(N):
    usage = int(input())
    left += (X - usage)

print(left + X)
