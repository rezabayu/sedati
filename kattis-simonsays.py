N = int(input())
hasil = []
for i in range(N):
    inst = input()
    if inst[0:10] == 'Simon says':
        result = inst[10::]
        hasil.append(result)

for doin in hasil:
    print(doin.strip())
