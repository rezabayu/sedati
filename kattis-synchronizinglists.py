results = []
while True:
    sets = int(input())
    if sets == 0:
        break
    list_a = []
    for i in range(sets*2):
        data = int(input())
        list_a.append(data)
    result = []
    list_1 = list_a[0:sets]
    list_2 = list_a[sets::]
    list_3 = list_1.copy()
    list_4 = list_2.copy()
    list_3.sort()
    list_4.sort()
    kamus = dict(zip(list_3,list_4))
    for dt in list_1:
        lto = kamus[dt]
        result.append(lto)
    results.append(result)

for li in results:
    for angka in li:
        print(angka)
    if results.index(li) == -1:
        break
    print()
