N = int(input())
final = []
for i in range(N):
    grup = input().split(" ")
    gn_grup = [int(x) for x in grup]
    for j in range(1,gn_grup[0]-1):
        if gn_grup[j+1] - gn_grup[j] != 1:
            final.append(j+1)
            break
for k in final:
    print(k)
