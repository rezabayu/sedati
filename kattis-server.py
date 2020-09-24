n, T = input().split(" ")
data = input().split(" ")
datask = [int(x) for x in data]
elaps = 0
for i in range(int(n)):
    elaps += datask[i]
    if elaps == int(T):
        print(i+1)
        break
    elif elaps > int(T):
        print(i)
        break
if elaps < int(T):
    print(i+1)
