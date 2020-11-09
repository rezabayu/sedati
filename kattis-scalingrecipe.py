T = int(input())
final = []
for i in range(T):
    hasil = []
    R, P, D = map(int, input().split(" "))
    SF = D / P
    rinci = []
    for j in range(R):
        bahan, berat, persen = input().split(" ")
        if float(persen) == 100:
            MW = float(berat) * SF
        rinci.append([bahan, float(berat), float(persen)])
    for k in range(R):
        hasil.append([rinci[k][0], rinci[k][2] * MW / 100])
    final.append(hasil)
for l in range(T):
    print("Recipe # %s" % (l+1))
    for m in range(len(final[l])):
        print(final[l][m][0], final[l][m][1])
    print('-' * 40)
