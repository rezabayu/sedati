line = int(input())
results = []
for i in range(line):
    data = input().split(" ")
    res = 0
    for j in range(len(data)):
        if int(data[j + 1]) < int(data[j]):
            break
        elif int(data[j + 1]) > int(data[j])*2:
            imp = int(data[j + 1]) - (int(data[j])*2)
            res += imp
    results.append(res)

for result in results:
    print(result)
