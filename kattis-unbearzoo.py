from collections import Counter
final = []
while True:
    n = int(input())
    if n == 0:
        break
    ani = []
    for i in range(n):
        kindo = input().split(" ")[-1]
        ani.append(kindo.lower())
    ani.sort()
    kount = Counter(ani)
    anak = []
    for a, b in kount.items():
        anak.append(a+" | "+str(b))
    final.append(anak)
for i in range(len(final)):
    print("List %s:" % (i+1))
    for j in final[i]:
        print(j)
