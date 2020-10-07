T = int(input())
results = []
for i in range(T):
    R, C = map(int, input().split(" "))
    draw = []
    for j in range(R):
        draw.append(input())
    has = []
    for k in draw[::-1]:
        has.append(k[::-1])
    results.append(has)
for l in range(T):
    print("Test %s" % (l+1))
    for m in results[l]:
        print(m)
