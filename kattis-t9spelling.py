N = int(input())
kamus = [' ', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
def translate(letter):
    for i in range(len(kamus)):
        if letter in kamus[i]:
            fore = (str(i)*(kamus[i].index(letter)+1))
            return fore, i

final_banget = []
for n in range(N):
    msg = input()
    hasil = []
    for num in range(len(msg)):
        fore, ifo = translate(msg[num])
        hasil.append([fore, ifo])

    finres = ""
    for i in range(len(hasil)):
        if i != 0 and hasil[i][1] == hasil[i-1][1]:
            finres += (" "+hasil[i][0])
        else:
            finres += hasil[i][0]
    final_banget.append(finres)

for num in range(1,len(final_banget)+1):
    print("Case #%s:" % num, final_banget[num-1])
